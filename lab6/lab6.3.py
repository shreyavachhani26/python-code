def count_digits(num):
    count = 0
    if num == 0:   # special case for 0
        return 1
    while num > 0:
        num //= 10   # remove last digit
        count += 1
    return count

# test the function
n = int(input("Enter a number: "))
print(f"The number of digits in {n} is {count_digits(n)}")
