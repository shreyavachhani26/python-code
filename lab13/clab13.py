# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 17:27:05 2025

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)
freq = 5

# Original signal
x = np.sin(2 * np.pi * freq * t)

# Time shift by 0.1 seconds
shift = 0.1
t_shifted = t + shift
x_shifted = np.sin(2 * np.pi * freq * t_shifted)

# Plot
plt.figure(figsize=(10,4))
plt.plot(t, x, label="Original")
plt.plot(t, x_shifted, label="Shifted (0.1s)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Time-Shifted Sine Wave (5 Hz)")
plt.legend()
plt.grid(True)
plt.show()
