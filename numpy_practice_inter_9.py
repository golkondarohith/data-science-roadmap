import numpy as np

data = np.getfromtxt('data.csv', delimiter=',', skip_header = 1 )

print("Data:\n", data)