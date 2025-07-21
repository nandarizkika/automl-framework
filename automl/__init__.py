
"""
AutoML Framework
A modular framework for automated machine learning.
"""

from .__version__ import __version__
from .utils import DataUtils, setup_logging
from .automl import AutoML
from .hyperparameter_tuner import HyperparameterTuner
from .automl_integration import TuningIntegrator

__all__ = ['AutoML', 'DataUtils', 'setup_logging', 'HyperparameterTuner', 'TuningIntegrator']