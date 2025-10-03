import numpy as np

arr = np.arange(36)
print("Array:\n",arr[:10])


new_arr = arr.reshape(6, 6)
print("Reshaped Array:\n", new_arr)