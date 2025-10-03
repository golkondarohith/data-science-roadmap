import numpy as np

#Generate 1000 random numbers from normal distribution(mean = 0, std=1)
data = np.random.normal(loc = 0, scale = 1, size=1000)

#Calculate statistics
mean_value = np.mean(data)
median_value = np.median(data)
variance_val = np.var(data)
std_val = np.std(data)


print("Mean: ", mean_value)
print("Median: ", median_value)
print("Variance: ", variance_val)
print("Standard Deviation: ", std_val)