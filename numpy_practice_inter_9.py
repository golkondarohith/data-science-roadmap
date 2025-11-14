import numpy as np

data = np.genfromtxt('data.csv', delimiter=',', skip_header = 1 )

print("Data:\n", data)

col_means = np.mean(data, axis=0)
print("\nMean of each column:", col_means)

max_row = data[np.argmax(data[:, 1])]
print("\nRow with maximum value in column 2:", max_row)