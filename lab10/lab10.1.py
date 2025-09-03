# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 10:36:23 2025

@author: ADMIN
"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Draw line plot
plt.plot(x, y, marker="o")

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")

# Show grid (optional, for better readability)
plt.grid(True)

# Display the plot
plt.show()
