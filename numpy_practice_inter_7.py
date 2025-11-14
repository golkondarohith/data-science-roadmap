import numpy as np

arr = np.array([-1, 4, 5, -4, 9, -2, 0, -7, -9])
print("Original Array:\n", arr)


arr[arr < 0] = 0
print("Non-negative Array", arr)