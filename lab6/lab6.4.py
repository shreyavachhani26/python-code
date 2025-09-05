num = int(input("Enter a number: "))

# find last digit
last_digit = num % 10

# find first digit
first_digit = num
while first_digit >= 10:
    first_digit //= 10

print(f"The first digit of {num} is {first_digit}")
print(f"The last digit of {num} is {last_digit}")
