num = int(input("Enter a number: "))
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10       # get last digit
    reverse = reverse * 10 + digit  # build reverse
    temp //= 10             # remove last digit

print(f"The reverse of {num} is {reverse}")
