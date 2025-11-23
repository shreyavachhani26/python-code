# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 20:56:05 2025

@author: ADMIN
"""

import numpy as np

# Poles of the system
poles = np.array([0.6, 0.4])

# Check stability
is_stable = np.all(np.abs(poles) < 1)

print("Poles:", poles)
print("Magnitudes:", np.abs(poles))
print("System is Stable?" , is_stable)
