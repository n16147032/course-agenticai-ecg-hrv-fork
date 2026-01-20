import numpy as np

# Shim for NumPy 2.0 compatibility
try:
    np.trapz = np.trapz
except AttributeError:
    np.trapz = np.trapezoid

from .agent import HRVCoachAgent
