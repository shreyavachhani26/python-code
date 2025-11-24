# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:26:40 2025

@author: ADMIN
"""

# check_dtypes.py
import pandas as pd

# Step A: Load the CSV file into a DataFrame
df = pd.read_csv('sample_data.csv')   # change name/path if needed

# Step B: Show the DataFrame (optional, to confirm correct load)
print("DataFrame contents:")
print(df)
print()  # blank line

# Step C: Show data types of each column (recommended)
print("Column data types (df.dtypes):")
print(df.dtypes)
print()

# Alternative: show more info (non-null counts + dtype) using df.info()
print("More detailed info (df.info()):")
df.info()
