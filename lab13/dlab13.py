# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 17:28:21 2025

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration
freq = 10  # 10 Hz sine wave

# Original sine wave
x = np.sin(2 * np.pi * freq * t)

# Scaled sine wave (amplitude × 3)
x_scaled = 3 * x

# Plot both signals
plt.figure(figsize=(10, 4))
plt.plot(t, x, label="Original (Amplitude = 1)")
plt.plot(t, x_scaled, label="Scaled (Amplitude = 3)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Scaled 10 Hz Sine Wave")
plt.legend()
plt.grid(True)
plt.show()
