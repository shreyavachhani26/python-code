# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 13:16:33 2025

@author: ADMIN
"""

filename = r"D:\Python\ict.txt"   # Your file name

lines_list = []   # empty list to store each line

try:
    with open(filename, "r") as file:
        for line in file:
            lines_list.append(line.strip())  # remove \n

    print("List of lines in the file:")
    print(lines_list)

except FileNotFoundError:
    print("File not found. Please check the path.")
