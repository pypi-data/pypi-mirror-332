# WeatherFlow v0.1.1

## Features
- Physics-guided attention for weather prediction
- Stochastic flow modeling
- Built-in ERA5 data support
- Comprehensive visualization tools
- Physics-constrained predictions

## Installation

## Quick Start

## Components
- Models:
  - PhysicsGuidedAttention
  - StochasticFlowModel
  - WeatherFlowPath
- Data Loading:
  - ERA5Dataset
  - WeatherDataset
- Visualization Tools:
  - WeatherVisualizer

- Fixed ERA5Dataset to properly handle anonymous access to WeatherBench2 data - Added explicit storage options for zarr data access - Improved error handling for data loading 