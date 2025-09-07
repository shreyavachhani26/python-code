import pandas as pd

# Create two Series
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

# Stack vertically (one below the other)
vertical_stack = pd.concat([s1, s2])
print("Vertical Stack:")
print(vertical_stack)

# Stack horizontally (side by side as columns in a DataFrame)
horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:")
print(horizontal_stack)
