# Q1 Creating a dictionary
student = {"Name": "Stuti", "Age": 18, "Marks": 91.5}
print(student, type(student))           # each key maps to one value

# Q2 Accessing values
print(student["Name"], student["Age"])
try:
    print(student["City"])
except KeyError as e:
    print("KeyError: key not found", e)

# Q3 get()
print(student.get("City", "Not available"))    # no error, returns default
print(student.get("Name"))

# Q4 Adding and updating
student["City"] = "Mumbai"
student["Marks"] = 95
print(student)

# Q5 Removing
print("pop:", student.pop("City"))
print(student)
print("pop missing key:", student.pop("Phone", "no such key"))

# Q6 Iterating
for k in student:
    print(k, end=" ")
print()
for v in student.values():
    print(v, end=" ")
print()
for k, v in student.items():
    print(k, "->", v)

# Q7 keys(), values(), items()
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

# Q8 Character frequency
text = input("Enter a string: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Q9 Nested dictionary
students = {
    "S1": {"name": "Asha", "marks": 80},
    "S2": {"name": "Ravi", "marks": 72},
}
print(students["S1"]["name"])
students["S2"]["marks"] = 78
print(students)

# Q10 Merging
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
d1.update(d2)
print(d1)                               # b is overwritten by d2's value

# Q11 Sorting
scores = {"Ravi": 72, "Asha": 80, "Meena": 65}
print(dict(sorted(scores.items())))                          # by key
print(dict(sorted(scores.items(), key=lambda x: x[1])))     # by value

# Q12 Inventory system
inventory = {"Pen": 50, "Notebook": 20}
inventory["Marker"] = 15
inventory["Pen"] += 25
del inventory["Notebook"]
print("Final inventory:", inventory)