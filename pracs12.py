# Q1 Basic try-except
try:
    a = float(input("Number 1: "))
    b = float(input("Number 2: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Q2 Different error types
try:
    x = int(input("Enter an integer: "))
    print("100 / x =", 100 / x)
except ValueError:
    print("Invalid input: please enter a whole number")
except ZeroDivisionError:
    print("Division by zero is not allowed")

# Q3 else block (runs only if no exception)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success, result =", result)

# Q4 finally (always runs)
try:
    f = open("temp.txt", "w")
    f.write("test")
    1 / 0
except ZeroDivisionError:
    print("An error occurred")
finally:
    f.close()
    print("File closed (finally always runs)")

# Q5 Exception details
for test in (lambda: 1 / 0, lambda: int("abc"), lambda: [1, 2][5], lambda: {"a": 1}["b"]):
    try:
        test()
    except Exception as e:
        print(type(e)._name_, "->", e)

# Q6 Loop until valid input
while True:
    try:
        n = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Not an integer, try again")
print("You entered:", n)

# Q7 User-friendly messages
op = input("Operation (add/div): ")
try:
    if op == "add":
        print(5 + 3)
    elif op == "div":
        print(5 / 0)
    else:
        raise ValueError("Unknown operation")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError as e:
    print("Invalid operation:", e)

# Q8 raise keyword
try:
    age = int(input("Age: "))
    if age < 18:
        raise Exception("You must be 18 or older")
    print("Access granted")
except Exception as e:
    print("Error:", e)

# Q9 Custom exception
class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("Marks: "))
    if marks > 100 or marks < 0:
        raise InvalidMarksError("Marks must be between 0 and 100")
    print("Valid marks:", marks)
except InvalidMarksError as e:
    print("Custom error:", e)
except ValueError:
    print("Please enter a number")

# Q10 Withdrawal with insufficient balance
class InsufficientBalance(Exception):
    pass
balance = 5000
try:
    amt = float(input("Withdraw amount: "))
    if amt > balance:
        raise InsufficientBalance(f"Balance is only {balance}")
    balance -= amt
    print("New balance:", balance)
except InsufficientBalance as e:
    print("Transaction failed:", e)
except ValueError:
    print("Enter a valid amount")

# Q11 Multiple except vs generic except
def multi(v):
    try:
        return 10 / int(v)
    except ValueError:
        return "multiple-except: not a number"
    except ZeroDivisionError:
        return "multiple-except: zero"
def generic(v):
    try:
        return 10 / int(v)
    except Exception:
        return "generic: something went wrong (cause unknown)"
for v in ("2", "abc", "0"):
    print(multi(v), "|", generic(v))

# Q12 Nested try-except
nums = [10, 20, 30]
try:
    d = int(input("Divisor: "))
    try:
        print("Result:", nums[1] / d)
        print("Index 5:", nums[5])
    except IndexError:
        print("Inner: index out of range")
except ValueError:
    print("Outer: divisor must be a number")
except ZeroDivisionError:
    print("Outer: divisor cannot be zero")
# Flow: the inner block handles IndexError; errors it does not handle move to the outer block.