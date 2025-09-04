# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 20:47:38 2025

@author: ADMIN
"""

# define a tuple
fruits = ("apple", "banana", "cherry", "orange")

# element to search
item = "banana"

# check existence using 'in' operator
if item in fruits:
    print(f"Yes, '{item}' exists in the tuple:", fruits)
else:
    print(f"No, '{item}' does not exist in the tuple:", fruits)
