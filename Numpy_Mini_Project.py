import numpy as np

data = np.genfromtxt('students.csv', delimiter = ",", skip_header = 1)

print(data)

marks = data[:, 3:]

# print(marks)
print("Mean scores:\n ", np.mean(marks, axis = 0))
print("Max scores:\n ", np.max(marks, axis=0))
print("Min scores:\n", np.min(marks, axis=0))

high_sci = data[data[:, 4] > 85]
print(high_sci)

totals = np.sum(marks, axis=1)
averages = np.mean(marks, axis=1)

print("Totals:", totals)
print("Avengers:", averages)

data[2, 3] = np.nan

col_means = np.nanmean(data[:, 3:], axis=0)
inds = np.where(np.isnan(data))
data[inds] = np.take(col_means, inds[1]-3)


print(data)

