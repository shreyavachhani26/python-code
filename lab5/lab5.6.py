# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 20:51:40 2025

@author: ADMIN
"""
# define a tuple
numbers = (5, 1, 4, 3, 2)

# sort the tuple using sorted(), then convert back to tuple
ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Original tuple:", numbers)
print("Sorted in ascending order:", ascending)
print("Sorted in descending order:", descending)
