import math

def evaluate_functions(x):
    f = math.cos(2 * x)
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)
    return f, f_prime, f_double_prime

# Evaluate at x = π
x = math.pi
f, f_prime, f_double_prime = evaluate_functions(x)

print(f"At x = π:")
print(f"f(x)        = {f}")
print(f"f'(x)       = {f_prime}")
print(f"f''(x)      = {f_double_prime}")
