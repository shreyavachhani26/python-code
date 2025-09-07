
# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find common elements using set intersection
common_items = list(set(list1) & set(list2))

# Display result
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common items: {common_items}")
