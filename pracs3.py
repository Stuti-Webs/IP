# Q1 Basic if
n = float(input("Number: "))
if n > 0:
    print("Positive number")

# Q2 If-else: even or odd
n = int(input("Integer: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3 elif ladder: grade
marks = float(input("Marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Q4 Nested if: voting eligibility
age = int(input("Age: "))
nationality = input("Nationality: ")
if age >= 18:
    if nationality.lower() == "indian":
        print("Eligible to vote")
    else:
        print("Not eligible: not an Indian citizen")
else:
    print("Not eligible: under 18")

# Q5 Largest of three (handles equal values)
a = float(input("First: "))
b = float(input("Second: "))
c = float(input("Third: "))
if a == b == c:
    print("All three are equal")
elif a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Q6 Leap year
year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Q7 Simple calculator
x = float(input("First number: "))
y = float(input("Second number: "))
op = input("Operator (+, -, *, /): ")
if op == "+":
    print("Result:", x + y)
elif op == "-":
    print("Result:", x - y)
elif op == "*":
    print("Result:", x * y)
elif op == "/":
    if y == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", x / y)
else:
    print("Invalid operator")

# Q8 Discount system
amount = float(input("Purchase amount: "))
if amount >= 2000:
    discount = 20
elif amount >= 1000:
    discount = 10
else:
    discount = 0
final = amount - amount * discount / 100
print(f"Discount: {discount}%, Final amount: {final:.2f}")

# Q9 Triangle type
s1 = float(input("Side 1: "))
s2 = float(input("Side 2: "))
s3 = float(input("Side 3: "))
if s1 == s2 == s3:
    print("Equilateral")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles")
else:
    print("Scalene")

# Q10 Menu-driven program
print("1. Even/Odd\n2. Largest of two\n3. Grade")
choice = input("Choice: ")
if choice == "1":
    n = int(input("Number: "))
    print("Even" if n % 2 == 0 else "Odd")
elif choice == "2":
    p = float(input("First: "))
    q = float(input("Second: "))
    print("Largest:", max(p, q))
elif choice == "3":
    m = float(input("Marks: "))
    if m >= 90:
        print("Grade A")
    elif m >= 75:
        print("Grade B")
    elif m >= 50:
        print("Grade C")
    else:
        print("Fail")
else:
    print("Invalid choice")