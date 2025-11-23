# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 17:25:45 2025

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt

# Sampling settings
fs = 500                         # Sampling frequency
t = np.linspace(0, 2, 2 * fs)    # 2 seconds duration

# Create signals
sine_5 = np.sin(2 * np.pi * 5 * t)      # 5 Hz sine wave
cosine_10 = np.cos(2 * np.pi * 10 * t)  # 10 Hz cosine wave

# Element-wise multiplication
product_signal = sine_5 * cosine_10

# Plot the result
plt.figure(figsize=(10, 5))
plt.plot(t, product_signal)
plt.title("Product of 5 Hz Sine Wave and 10 Hz Cosine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
