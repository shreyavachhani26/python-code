n = int(input("Enter a positive integer: "))

# initialize sum
total = 0
i = 1

# use while loop to add numbers from 1 to n
while i <= n:
    total += i
    i += 1

print(f"The sum of natural numbers from 1 to {n} is {total}")
