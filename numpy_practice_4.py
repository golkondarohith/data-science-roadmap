import numpy as np

arr = np.random.randint(1, 101, size=10)
print("Array:\n", arr)

even_arr = arr[arr % 2 == 0]
print("Even numbers array:\n", even_arr)