import torch
from torch.utils.data import Dataset
import xarray as xr
import numpy as np
import h5py
import fsspec
import gcsfs
import os
import logging
from pathlib import Path
from typing import List, Dict, Tuple, Union, Optional, Any

# Configure logging
logger = logging.getLogger(__name__)

class WeatherDataset(Dataset):
    """Dataset class for loading weather data from HDF5 files.
    
    This class provides a flexible interface for loading meteorological data
    from HDF5 files with robust error handling and logging.
    """

    def __init__(
        self, 
        data_path: str, 
        variables: List[str],
        raise_on_missing: bool = False,
        normalize: bool = False,
        normalization_stats: Optional[Dict[str, Dict[str, float]]] = None
    ):
        """Initialize the dataset.
        
        Args:
            data_path: Path to the data directory
            variables: List of variable names to load
            raise_on_missing: Whether to raise an exception if a file is missing
            normalize: Whether to normalize the data
            normalization_stats: Dictionary of normalization statistics for each variable
                in the format {var_name: {'mean': float, 'std': float}}
        """
        self.data_path = Path(data_path)
        self.variables = variables
        self.raise_on_missing = raise_on_missing
        self.normalize = normalize
        self.normalization_stats = normalization_stats or {}
        
        # Initialize data dictionary
        self.data = {}
        
        # Load the data
        self._load_data()

    def _load_data(self) -> None:
        """Load data from HDF5 files with robust error handling."""
        for var in self.variables:
            file_path = self.data_path / f"{var}_train.h5"
            
            try:
                if file_path.exists():
                    with h5py.File(file_path, "r") as f:
                        # Load the data
                        data = np.array(f[var])
                        
                        # Apply normalization if requested
                        if self.normalize and var in self.normalization_stats:
                            stats = self.normalization_stats[var]
                            data = (data - stats['mean']) / stats['std']
                            
                        self.data[var] = data
                        logger.info(f"Successfully loaded {var} data with shape {data.shape}")
                else:
                    error_msg = f"File {file_path} not found."
                    if self.raise_on_missing:
                        raise FileNotFoundError(error_msg)
                    else:
                        logger.warning(error_msg)
            except Exception as e:
                error_msg = f"Error loading {var} data: {str(e)}"
                if self.raise_on_missing:
                    raise RuntimeError(error_msg) from e
                else:
                    logger.warning(error_msg)
        
        if not self.data:
            raise RuntimeError(f"No data was loaded from {self.data_path}")

    def __len__(self) -> int:
        """Return the number of samples in the dataset."""
        if not self.data:
            return 0
        # Use the first variable to determine length
        return len(next(iter(self.data.values())))

    def __getitem__(self, idx: int) -> Dict[str, np.ndarray]:
        """Get a sample from the dataset.
        
        Args:
            idx: Index of the sample to retrieve
            
        Returns:
            Dictionary mapping variable names to their data arrays
        """
        if idx < 0 or idx >= len(self):
            raise IndexError(f"Index {idx} out of range for dataset of length {len(self)}")
            
        return {var: data[idx] for var, data in self.data.items()}
    
    @property
    def shape(self) -> Dict[str, Tuple[int, ...]]:
        """Return the shape of each variable in the dataset."""
        return {var: data.shape for var, data in self.data.items()}
    
    def to_tensor(self, sample: Dict[str, np.ndarray]) -> Dict[str, torch.Tensor]:
        """Convert a sample to PyTorch tensors.
        
        Args:
            sample: Dictionary mapping variable names to numpy arrays
            
        Returns:
            Dictionary mapping variable names to PyTorch tensors
        """
        return {var: torch.tensor(data, dtype=torch.float32) 
                for var, data in sample.items()}
    
    def get_batch(self, indices: List[int]) -> Dict[str, torch.Tensor]:
        """Get a batch of samples.
        
        Args:
            indices: List of indices to include in the batch
            
        Returns:
            Dictionary mapping variable names to batched PyTorch tensors
        """
        samples = [self[i] for i in indices]
        batch = {}
        
        for var in self.variables:
            if var in samples[0]:
                batch[var] = torch.stack([torch.tensor(s[var], dtype=torch.float32) 
                                         for s in samples])
        
        return batch
