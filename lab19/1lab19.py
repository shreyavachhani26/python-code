# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 20:54:36 2025

@author: ADMIN
"""

import sympy as sp

def z_transform_unit_step():
    # Define symbols
    n, z = sp.symbols('n z')

    # Unit step u[n] = 1 for n>=0
    u = 1  

    # Compute Z-transform
    U_z = sp.summation(u * z**(-n), (n, 0, sp.oo))
    U_z_simplified = sp.simplify(U_z)

    print("Z-transform of unit step u[n]:")
    print("U(z) =", U_z_simplified)

    # Find pole
    denominator = sp.denom(U_z_simplified)
    poles = sp.solve(denominator, z)
    print("Poles:", poles)

    # Stability check
    stable = all(abs(complex(p)) < 1 for p in poles)

    if stable:
        print("System is STABLE")
    else:
        print("System is UNSTABLE (or marginally stable)")

# Run function
z_transform_unit_step()
