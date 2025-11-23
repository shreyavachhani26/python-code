# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 17:29:09 2025

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time axis (1 second)
freq = 5  # 5 Hz sine wave

# Original sine wave
x = np.sin(2 * np.pi * freq * t)

# Time-reversed signal
x_rev = x[::-1]          # Reverse the samples
t_rev = t[::-1]          # Reverse the time axis

# Plot both signals
plt.figure(figsize=(10, 4))
plt.plot(t, x, label="Original Signal")
plt.plot(t_rev, x_rev, label="Reversed Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Time-Reversed 5 Hz Sine Wave")
plt.legend()
plt.grid(True)
plt.show()
