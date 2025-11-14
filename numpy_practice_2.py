import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))
print("Matrix\n", matrix)

element = matrix[1, 2]
print("\nElement at 2nd row, 3rd column: ", element)