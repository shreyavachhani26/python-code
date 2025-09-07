
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Display result
print("Frequency of elements:")
for key, value in frequency.items():
    print(f"{key}: {value}")
