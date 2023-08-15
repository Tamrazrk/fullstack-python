import math

x = int(input("Enter the Number: "))

sum_of_divs = 1
for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
        sum_of_divs += i + x // i * (x // i != i)

print(f"{x} is{' not' if x != sum_of_divs else ''} perfect number")
