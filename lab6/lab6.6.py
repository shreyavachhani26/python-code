num = int(input("Enter a number: "))

product = 1
temp = num


if num == 0:
    product = 0
else:
    while temp > 0:
        digit = temp % 10     # get last digit
        product *= digit      # multiply with product
        temp //= 10           # remove last digit

print(f"The product of digits of {num} is {product}")
