# Q1 for loop and range
for i in range(1, 11):
    print(i, end=" ")
print()
for i in range(2, 11, 2):          # range(start, stop, step)
    print(i, end=" ")
print()

# Q2 while loop (same as Q1)
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# Q3 Sum and average
n = int(input("How many numbers: "))
total = 0
for _ in range(n):
    total += float(input("Number: "))
print("Sum:", total, "Average:", total / n)

# Q4 Factorial (for and while)
num = int(input("Number for factorial: "))
f = 1
for i in range(1, num + 1):
    f *= i
print("Factorial (for):", f)
f = 1
i = 1
while i <= num:
    f *= i
    i += 1
print("Factorial (while):", f)

# Q5 Multiplication table
t = int(input("Table of: "))
for i in range(1, 11):
    print(f"{t} x {i:2} = {t * i}")

# Q6 Reverse and palindrome
num = int(input("Number: "))
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reverse:", rev)
print("Palindrome" if rev == num else "Not a palindrome")

# Q7 Count digits, even and odd
num = abs(int(input("Number: ")))
digits = even = odd = 0
for d in str(num):
    digits += 1
    if int(d) % 2 == 0:
        even += 1
    else:
        odd += 1
print("Digits:", digits, "Even:", even, "Odd:", odd)

# Q8 Prime checker (check only up to square root)
num = int(input("Number: "))
prime = num > 1
i = 2
while i * i <= num:
    if num % i == 0:
        prime = False
        break
    i += 1
print("Prime" if prime else "Not prime")

# Q9 Fibonacci
terms = int(input("Terms: "))
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()

# Q10 Nested loop patterns
rows = 4
for i in range(1, rows + 1):
    print("* " * i)
for i in range(rows, 0, -1):         # reverse pattern
    print("* " * i)
for i in range(1, rows + 1):         # number pattern
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(rows, 0, -1):         # reverse number pattern
    for j in range(1, i + 1):
        print(j, end=" ")
    print()