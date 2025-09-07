
# Sample list
numbers = [1, 2, 3, 4, 5]

# Convert list to string, then to integer
single_integer = int("".join(map(str, numbers)))

# Display result
print(f"List: {numbers}")
print(f"Single integer: {single_integer}")
