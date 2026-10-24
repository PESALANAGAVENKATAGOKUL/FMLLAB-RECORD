import numpy as np

print(
    "1D Array:\n", np.array([1, 2, 3, 4, 5]), "\n\n",
    "2D Array:\n", np.array([[1, 2, 3], [4, 5, 6]]), "\n\n",
    "Zeros:\n", np.zeros((3, 3)), "\n\n",
    "Ones:\n", np.ones((2, 4)), "\n\n",
    "Identity:\n", np.eye(3), "\n\n",
    "Range:\n", np.arange(0, 10, 2)
)
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(
    "Array a:", a, "\n",
    "Array b:", b, "\n\n",
    "Addition (a + b):", a + b, "\n",
    "Multiplication (a * b):", a * b, "\n",
    "Scalar Multiplication (a * 10):", a * 10, "\n\n",
    "Square Root of a:", np.sqrt(a), "\n",
    "Mean of a:", np.mean(a), "\n",
    "Dot Product (a · b):", np.dot(a, b)
)
import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(
    "Matrix:\n", matrix, "\n\n",
    "Element at [1,2]:", matrix[1, 2], "\n\n",
    "First Row:", matrix[0, :], "\n",
    "Second Column:", matrix[:, 1], "\n\n",
    "Top-left 2x2 Sub-matrix:\n", matrix[0:2, 0:2]
)
