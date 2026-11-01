# Q1 Defining and calling a function
def greet():
    print("Hello from a function!")
greet()
greet()                                  # reuse without rewriting

# Q2 Parameters
def add(a, b):
    print("Sum:", a + b)
add(int(input("First: ")), int(input("Second: ")))

# Q3 Return values
def square(n):
    return n * n
result = square(6)
print("Square:", result, "| Double of square:", result * 2)

# Q4 Default and keyword arguments
def intro(name, city="Mumbai"):
    print(f"{name} lives in {city}")
intro("Stuti")                           # positional, default city
intro("Asha", "Pune")                    # positional
intro(city="Delhi", name="Ravi")         # keyword, order does not matter

# Q5 Built-in functions
lst = [4, 9, 1, 7]
print(len(lst), sum(lst), max(lst), min(lst))
print(len("python"), max("python"))
total = 0
for x in lst:
    total += x
print("Manual sum:", total)              # built-ins are shorter and faster

# Q6 List processing
def list_sum(l):
    return sum(l)
def largest(l):
    big = l[0]
    for x in l:
        if x > big:
            big = x
    return big
print(list_sum(lst), largest(lst))
print(list_sum([1, 2, 3]), largest([5, 50, 15]))

# Q7 Recursive factorial
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)               # fact(4) -> 4*fact(3) -> 4*3*fact(2) ...
print("Factorial of 5:", fact(5))

# Q8 Recursive Fibonacci
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)       # slow for big n: repeats the same work
print([fib(i) for i in range(10)])

# Q9 Functions calling functions
def get_input():
    return int(input("Enter a number: "))
def process(n):
    return n * n
def show(r):
    print("Result:", r)
def main():
    show(process(get_input()))
main()

# Q10 Local vs global scope
count = 0
def change_local():
    count = 100                          # creates a new local variable
    print("Inside (local):", count)
def change_global():
    global count
    count = 100
change_local()
print("After local change:", count)
change_global()
print("After global change:", count)

# Q11 Menu-driven program
def add2(a, b):
    return a + b
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
print("1. Add  2. Prime check  3. Factorial")
ch = input("Choice: ")
if ch == "1":
    print(add2(int(input("A: ")), int(input("B: "))))
elif ch == "2":
    print("Prime" if is_prime(int(input("Number: "))) else "Not prime")
elif ch == "3":
    print(factorial(int(input("Number: "))))
else:
    print("Invalid choice")

# Q12 Student result system
def input_marks():
    return [float(input(f"Marks {i}: ")) for i in (1, 2, 3)]
def calculate(marks):
    total = sum(marks)
    return total, total / len(marks)
def grade(p):
    if p >= 90: return "A"
    if p >= 75: return "B"
    if p >= 50: return "C"
    return "Fail"
m = input_marks()
t, p = calculate(m)
print(f"Total: {t}, Percentage: {p:.2f}%, Grade: {grade(p)}")