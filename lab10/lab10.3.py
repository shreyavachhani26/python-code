# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 10:40:27 2025

@author: ADMIN
"""

import matplotlib.pyplot as plt

# Sample data
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create bar chart
plt.bar(languages, popularity, color="purple")

# Add labels and title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")

# Show grid (optional)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Display the chart
plt.show()
