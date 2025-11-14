import numpy as np



#List method

# temperatures = [34.4, 32.76, 27.98, 41.76, 29.98]
# total = 0
# for temp in temperatures:
#     total += temp
# average = total/len(temperatures)
# print(average)

#numpy method

temperatures = np.array([34.4, 32.76, 27.98, 41.76, 29.98])
average = np.mean(temperatures)
print(average)