# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 17:24:22 2025

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt

# Sampling and time
fs = 1000                 # Sampling frequency
t = np.linspace(0, 1, fs) # 1 second duration

# Sine waves
sine_5 = np.sin(2 * np.pi * 5 * t)    # 5 Hz signal
sine_10 = np.sin(2 * np.pi * 10 * t)  # 10 Hz signal

# Combined signal
combined = sine_5 + sine_10

# Plotting
plt.figure(figsize=(10, 7))

plt.subplot(3, 1, 1)
plt.plot(t, sine_5)
plt.title("Sine Wave – 5 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, sine_10)
plt.title("Sine Wave – 10 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t, combined)
plt.title("Combined Signal (5 Hz + 10 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
