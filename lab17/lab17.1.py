# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:14:50 2025

@author: ADMIN
"""

import sympy as sp

# Define symbols
n, z = sp.symbols('n z')

# Define the sequence x[n] = 3^n u[n]
x_n = 3**n   # u[n] ensures n >= 0, so summation starts at 0

# Compute Z-transform: X(z) = Σ (3^n * z^(-n)), n=0..∞
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

# Print the result
print("Z-transform of x[n] = 3^n u[n]:")
sp.pprint(X_z.simplify(), use_unicode=True)
