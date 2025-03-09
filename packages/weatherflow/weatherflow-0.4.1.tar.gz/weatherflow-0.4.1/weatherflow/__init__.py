# weatherflow/__init__.py
"""WeatherFlow: A Deep Learning Library for Weather Prediction.

This package provides tools for weather data processing, model building,
and visualization with a focus on deep learning approaches.
"""

from .version import __version__, get_version
from .data import WeatherDataset, ERA5Dataset, create_data_loaders
from .models import (
    BaseWeatherModel,
    WeatherFlowMatch,
    PhysicsGuidedAttention,
    StochasticFlowModel
)
from .utils.visualization import WeatherVisualizer
from .utils.flow_visualization import FlowVisualizer
from .utils.evaluation import WeatherEvaluator
from .manifolds.sphere import Sphere
from .training.flow_trainer import FlowTrainer

__author__ = "Eduardo Siman"
__email__ = "esiman@msn.com"
__license__ = "MIT"

__all__ = [
    # Version
    "__version__",
    "get_version",
    
    # Data
    "WeatherDataset",
    "ERA5Dataset",
    "create_data_loaders",
    
    # Models
    "BaseWeatherModel",
    "WeatherFlowMatch",
    "PhysicsGuidedAttention",
    "StochasticFlowModel",
    
    # Utilities
    "WeatherVisualizer",
    "FlowVisualizer",
    "WeatherEvaluator",
    
    # Manifolds
    "Sphere",
    
    # Training
    "FlowTrainer"
]
