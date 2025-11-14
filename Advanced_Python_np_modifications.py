import numpy as np

#array - original array
# index - 
# value - 
# axis - 
# axis = 0 row-wise
# azis = 1 col-wise

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)

new_arr = np.insert(arr, 2, 100)
print(new_arr)


new_arr2 = np.append(arr, [70, 80])
print(new_arr2)


#Concatenation
con_arr = np.concatenate((arr, new_arr))
print(con_arr)