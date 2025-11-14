import numpy as np

arr = np.random.randint(1, 101, size = 10)
print("Original array: \n", arr)

count = np.sum(arr % 5 == 0)
print("Count: \n", count)