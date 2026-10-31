#Creating valid variables
name="Stuti"
age=18
marks=91.5
city="Mumbai"

#Displaying values
print("Name:",name)
print("Age:",age)
print("Marks:",marks)
print("City:",city)
# Q1 Valid variables
name = "Stuti"
age = 18
marks = 91.5
city = "Mumbai"
print(name, age, marks, city)
# Invalid names (they crash, so they stay as comments):
# 1name = "x"    # cannot start with a digit
# class = 5      # reserved keyword
# my-name = "x"  # hyphen not allowed

# Q2 Dynamic typing
x = 10
print(type(x))
x = "Python"
print(type(x))
x = 3.14
print(type(x))

# Q3 Constants (Python does not enforce them)
PI = 3.14
GRAVITY = 9.8
MAX_USERS = 100
PI = 3.15  # allowed; capital letters are only a convention
print(PI, GRAVITY, MAX_USERS)

# Q4 Data type identification
i = int(input("Integer: "))
f = float(input("Float: "))
s = input("String: ")
b = input("Boolean (True/False): ") == "True"
print("Value\tType")
for v in (i, f, s, b):
    print(v, "\t", type(v)._name_)

# Q5 Type conversion
age = int(input("Age: "))
marks = float(input("Marks: "))
print(age + 5, marks + 5)
try:
    print(input("Age again: ") + 5)
except TypeError as e:
    print("Error:", e)

# Q6 Implicit vs explicit
print(5 + 2.5)               # implicit: int becomes float
try:
    print(5 + "5")
except TypeError as e:
    print("Error:", e)
print(5 + int("5"))          # explicit fix
print(str(5) + "5")

# Q7 Memory behaviour
a = 10
b = 10
print(id(a), id(b))          # same id
b = 20
print(id(a), id(b))          # b now points elsewhere

# Q8 Swapping
a, b = 5, 10
t = a; a = b; b = t
print("Third variable:", a, b)
a, b = b, a
print("Tuple unpacking:", a, b)

# Q9 Type-based calculator
def conv(v):
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v

p = conv(input("First: "))
q = conv(input("Second: "))
if isinstance(p, (int, float)) and isinstance(q, (int, float)):
    print("Sum:", p + q)
elif isinstance(p, str) and isinstance(q, str):
    print("Joined:", p + q)
else:
    print("Invalid: mixed types")

# Q10 Boolean logic
age = 20
marks = 45
is_adult = age > 18
passed = marks > 50
print(is_adult, passed)
if is_adult:
    print("Adult")
if passed:
    print("Pass")
else:
    print("Fail")

# Q11 Temperature converter
c = float(input("Celsius: "))
fh = c * 9 / 5 + 32
print(f"{c:.1f} C = {fh:.2f} F")