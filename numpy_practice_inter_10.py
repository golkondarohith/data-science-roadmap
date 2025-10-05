import numpy as np

#Create two matrices
A = np.array([[1, 2, 3],
             [4, 5, 6]])

B = np.array([[7, 8],
             [9, 10],
             [11, 12]])

#Matrix multiplication
C = np.dot(A, B)

print("Matrix A: \n", A)
print("Matrix B: \n", B)
print("Matrix C: \n", C)