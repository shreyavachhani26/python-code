num = int(input("Enter a number: "))
num_str = str(num)

if len(num_str) == 1:
    swapped = num_str
else:
    # swap first and last characters
    swapped = num_str[-1] + num_str[1:-1] + num_str[0]

print(f"Original number: {num}")
print(f"After swapping first and last digits: {swapped}")
