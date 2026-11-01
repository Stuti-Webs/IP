# Q1 Input and output: print vs f-string
name = input("Name: ")
age = int(input("Age: "))
print("Name:", name, "Age:", age)
print(f"Name: {name}, Age: {age}")

# Q2 Numeric input handling
a = input("First number: ")
b = input("Second number: ")
print("Without conversion:", a + b)      # joins text, wrong result
a = float(a)
b = float(b)
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b if b != 0 else "Cannot divide by zero")

# Q3 Expression evaluation
x = float(input("Number 1: "))
y = float(input("Number 2: "))
z = float(input("Number 3: "))
print("Sum:", x + y + z)
print("Average:", (x + y + z) / 3)
print("(a + b) * c / 2 =", (x + y) * z / 2)

# Q4 Operator precedence
print(10 + 5 * 2)        # 20  (* before +)
print((10 + 5) * 2)      # 30  (brackets first)
print(100 / 5 + 3 * 2)   # 26.0 (20.0 + 6)

# Q5 Salary breakdown
basic = float(input("Basic salary: "))
hra = basic * 0.20
da = basic * 0.10
net = basic + hra + da
print(f"Basic: {basic:.2f}\nHRA (20%): {hra:.2f}\nDA (10%): {da:.2f}\nNet salary: {net:.2f}")

# Q6 Area and perimeter
l = float(input("Rectangle length: "))
w = float(input("Rectangle width: "))
print(f"Rectangle area: {l * w:.2f}, perimeter: {2 * (l + w):.2f}")
r = float(input("Circle radius: "))
pi = 3.14159
print(f"Circle area: {pi * r * r:.2f}, circumference: {2 * pi * r:.2f}")

# Q7 Unit conversion
km = float(input("Kilometers: "))
print(f"{km} km = {km * 1000} m")
c = float(input("Celsius: "))
print(f"{c} C = {c * 9 / 5 + 32:.2f} F")
rs = float(input("Rupees: "))
print(f"{rs} Rs = {rs / 83:.2f} USD (rate: 1 USD = 83 Rs)")

# Q8 Multiple inputs in one line
nums = input("Enter a, b, c separated by commas: ").split(",")
p, q, s = [float(n) for n in nums]
print(f"Sum = {p + q + s}, Product = {p * q * s}")

# Q9 Grading system
m1 = float(input("Marks 1: "))
m2 = float(input("Marks 2: "))
m3 = float(input("Marks 3: "))
total = m1 + m2 + m3
percent = total / 3
if percent >= 90:
    grade = "A"
elif percent >= 75:
    grade = "B"
elif percent >= 50:
    grade = "C"
else:
    grade = "Fail"
print(f"Total: {total}, Percentage: {percent:.2f}%, Grade: {grade}")

# Q10 Error analysis
# print(10 / 0)      # ZeroDivisionError
# print("5" + 3)     # TypeError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: cannot divide by zero")
try:
    print("5" + 3)
except TypeError:
    print("Error: cannot add string and number")
    print("Fixed:", int("5") + 3)