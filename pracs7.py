import numpy as np

# Q1 Creating lists and tuples
nums = [10, 20, 30, 40, 50]
words = ("apple", "banana", "cherry")
print(nums, type(nums))
print(words, type(words))            # [] makes a list, () makes a tuple

# Q2 Indexing (positive and negative)
print(nums[0], nums[-1], nums[len(nums) // 2])
print(words[0], words[-1], words[1])

# Q3 Slicing
print(nums[:3], nums[-2:], nums[::2])
print(words[:3], words[-2:], words[::2])

# Q4 Mutability vs immutability
nums[0] = 99
print("List changed:", nums)
try:
    words[0] = "mango"
except TypeError as e:
    print("Tuple error:", e)          # tuples cannot be changed after creation

# Q5 Adding to a list
nums.append(60)
nums.insert(1, 15)
print(nums)

# Q6 Removing from a list
nums.remove(15)
print("popped:", nums.pop())
print(nums)
try:
    nums.remove(1000)
except ValueError as e:
    print("Error:", e)

# Q7 sort() and reverse()
data = [5, 2, 9, 1, 7]
data.sort()
print("Ascending:", data)
data.sort(reverse=True)
print("Descending:", data)
data.reverse()
print("Reversed:", data)

# Q8 Tuple methods
t = (1, 2, 2, 3, 2)
print("count of 2:", t.count(2), "index of 3:", t.index(3))
if 9 in t:
    print(t.index(9))
else:
    print("9 is not in the tuple")

# Q9 Nested lists
grid = [[1, 2, 3], [4, 5, 6]]
print(grid[1][2])
grid[0][0] = 100
print(grid)

# Q10 Converting between list and tuple
tup = tuple(nums)
lst = list(tup)
lst.append(777)
print(tup, lst)

# Q11 Iterating
for x in nums:
    print(x, end=" ")
print()
total = 0
for x in nums:
    total += x
print("Sum:", total)
for w in words:
    print(w, end=" ")
print()

# Q12 Shopping cart
categories = ("Fruits", "Dairy", "Snacks")
cart = ["Apple", "Milk"]
cart.append("Chips")
cart.remove("Apple")
print("Categories:", categories)
print("Cart:", cart, "| Items:", len(cart))

# ---- Part B: 2D indexing and slicing ----
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B1 Basic indexing
print(matrix[0][0], matrix[-1][-1], matrix[1][1])
# B2 Row and column access
print("2nd row:", matrix[1])
for row in matrix:
    print(row[2], end=" ")             # column needs a loop: lists store rows, not columns
print()
# B3 Negative indexing
print(matrix[-1], [r[-1] for r in matrix], matrix[-1][-1])
# B4 Slicing rows
print(matrix[:2], matrix[-2:])
# B5 Submatrix with slicing + loop
sub = [row[0:2] for row in matrix[0:2]]
print(sub)                              # lists cannot slice rows and columns at once
# B6 NumPy indexing
arr = np.array(matrix)
print(arr[1, 2], arr[1], arr[:, 2])
# B7 NumPy slicing
print(arr[0:2], arr[:, -1])
# B8 Submatrix extraction
print(arr[1:3, 1:3])                    # one short line, no loops needed