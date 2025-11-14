import numpy as np

x = np.array([3, 5, 7, 9, 19])
y = np.array([2, 4, 6, 8, 18])

corr_matrix = np.corrcoef(x, y)
print("Correlation Matrix:\n ", corr_matrix)