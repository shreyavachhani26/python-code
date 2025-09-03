# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 10:38:53 2025

@author: ADMIN
"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]

# Two different lines
y1 = [2, 4, 6, 8, 10]       # line 1 (y = 2x)
y2 = [1, 4, 9, 16, 25]      # line 2 (y = x^2)

# Plot both lines
plt.plot(x, y1, label="y = 2x", marker="o")
plt.plot(x, y2, label="y = x^2", marker="s")

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Line Plots")

# Add legend to distinguish lines
plt.legend()

# Show grid (optional)
plt.grid(True)

# Display the plot
plt.show()
