# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:30:00 2025

@author: ADMIN
"""

import pandas as pd

# Sample DataFrame with missing values
df = pd.DataFrame({
    'Age': [25, None, 30, None, 40]
})

# Calculate the mean of the column
mean_value = df['Age'].mean()

# Fill missing values with the mean
df['Age'] = df['Age'].fillna(mean_value)

# Display the updated DataFrame
print("Data after filling missing values with mean:")
print(df)
