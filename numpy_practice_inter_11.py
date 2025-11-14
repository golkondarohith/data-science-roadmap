import numpy as np

#Square matrix
M = np.array([[4, 2],
              [3, 1]])

#Determinant
det = np.linalg.det(M)
print("Determinant: \n", det)


#Inverse
inv = np.linalg.inv(M)
print("Inverse: \n", inv)

#eigen values and eigen vectors
eigenvalues, eigenvectors = np.linalg.eig(M)
print("Eigenvalues: \n", eigenvalues)
print("Eigenvectors: \n", eigenvectors)