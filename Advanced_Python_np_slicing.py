import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])


print(arr[3:6])
print(arr[:])
print(arr[:4])
print(arr[::2])
print(arr[::-1])

#Boolean Masking
print(arr[arr > 25])