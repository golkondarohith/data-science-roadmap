import numpy as np

arr_2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


arr_1d = arr_2d.flatten()

arr_1d_ravel = arr_2d.ravel()

print("2D Array:\n", arr_2d)
print("Flatten Array:\n", arr_1d)
print("Flatten Array(Ravel):\n", arr_1d_ravel)