# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 13:25:17 2025

@author: ADMIN
"""

import csv

filename = r"D:\Python\data-1.csv"   # your CSV file name

try:
    with open(filename, "r") as file:
        reader = csv.reader(file)

        print("CSV File Content:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found. Please check the path.")






















