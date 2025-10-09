# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:16:07 2025

@author: ADMIN
"""

import sympy as sp

# Define symbols
n, z, w = sp.symbols('n z w', real=True)

# Define the sequence x[n] = cos(w n) u[n]
x_n = sp.cos(w * n)

# Z-transform: X(z) = Σ (cos(w n) * z^(-n)), n=0..∞
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

# Simplify and display result
print("Z-transform of x[n] = cos(wn) u[n]:")
sp.pprint(sp.simplify(X_z), use_unicode=True)
