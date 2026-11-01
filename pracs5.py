# Q1 break
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print()

# Q2 continue
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# Q3 break vs continue (same condition i == 5)
print("With break:", end=" ")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print()
print("With continue:", end=" ")
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()
# break stops the whole loop; continue skips only that one turn.

# Q4 Search in a list
lst = [int(x) for x in input("Numbers separated by spaces: ").split()]
target = int(input("Search for: "))
for pos, val in enumerate(lst):
    if val == target:
        print(f"Found at position {pos + 1}")
        break
else:
    print("Not found")

# Q5 First number from 1-100 divisible by n
n = int(input("Divisible by: "))
for i in range(1, 101):
    if i % n == 0:
        print("First number:", i)
        break

# Q6 Skip negatives
nums = [int(x) for x in input("Numbers separated by spaces: ").split()]
for x in nums:
    if x < 0:
        continue
    print(x, end=" ")
print()

# Q7 Sum of valid inputs (ignore negatives, stop at 0)
total = 0
while True:
    x = float(input("Enter number (0 to stop): "))
    if x == 0:
        break
    if x < 0:
        continue
    total += x
print("Sum of valid inputs:", total)

# Q8 Password retry (3 attempts)
for attempt in range(1, 4):
    if input("Password: ") == "python123":
        print("Login successful")
        break
    print(f"Wrong password ({attempt}/3)")
else:
    print("Account locked after 3 failed attempts")

# Q9 pass in an empty block
for i in range(5):
    if i == 2:
        pass          # placeholder; without pass, an empty block is a SyntaxError
    print(i, end=" ")
print()

# Q10 Pattern with conditional skipping
for i in range(1, 6):
    for j in range(1, 6):
        if j % 2 == 0:
            continue
        print(j, end=" ")
    print()