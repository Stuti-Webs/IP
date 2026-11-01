import numpy as np

# Q1 Create and access a 3x3 matrix
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", m)
print("First row:", m[0])
print("Element at (2,3):", m[1][2])

# Q2 Traversal
print("Row-wise:")
for row in m:
    for x in row:
        print(x, end=" ")
    print()
print("Column-wise:")
for j in range(3):
    for i in range(3):
        print(m[i][j], end=" ")
    print()

# Q3 Sum of rows and columns
for i in range(3):
    print(f"Row {i + 1} sum:", sum(m[i]))
for j in range(3):
    print(f"Column {j + 1} sum:", sum(m[i][j] for i in range(3)))

# Q4 Matrix addition
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        result[i][j] = a[i][j] + b[i][j]
print("A + B =", result)

# Q5 Transpose
mat = [[1, 2, 3], [4, 5, 6]]
t = [[mat[i][j] for i in range(2)] for j in range(3)]
print("Original:", mat)
print("Transpose:", t)

# Q6 NumPy array creation
x1 = np.array([1, 2, 3])
x2 = np.zeros((2, 3))
x3 = np.ones((3, 2))
for arr in (x1, x2, x3):
    print(arr, "shape:", arr.shape, "dtype:", arr.dtype)

# Q7 Indexing and slicing
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Element [1,2]:", arr[1, 2])
print("Row 0:", arr[0])
print("Column 1:", arr[:, 1])
print("Slice rows 0-1, cols 1-2:\n", arr[0:2, 1:3])

# Q8 Arithmetic on arrays
p = np.array([1, 2, 3])
q = np.array([4, 5, 6])
print("Add:", p + q, "Subtract:", p - q, "Multiply:", p * q)
print("Lists + joins them:", [1, 2, 3] + [4, 5, 6])  # lists do not add element-wise

# Q9 Statistics
data = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(data), "Median:", np.median(data), "Std dev:", np.std(data))

# Q10 Reshape
r = np.arange(1, 13)
print(r.reshape(3, 4))
print(r.reshape(4, 3))
# r.reshape(5, 3) would fail: 12 elements cannot fill 15 slots

# Q11 Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A x B:\n", A @ B)
print("Transpose of A:\n", A.T)

# Q12 Dataset analysis (student marks)
marks = np.array([[80, 90, 70], [60, 75, 85], [95, 88, 92]])
print("Average per student:", marks.mean(axis=1))
print("Highest:", marks.max(), "Lowest:", marks.min())
print("Top scorer is student", marks.sum(axis=1).argmax() + 1)