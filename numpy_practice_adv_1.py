import numpy as np

#Number of simulations
num_rolls = 10000

#Simulata rolling two dice
die1 = np.random.randint(1, 7, num_rolls)
die2 = np.random.randint(1, 7, num_rolls)

#Calculate their sum
sums = die1 + die2

#Count how many times the sum equals 7
count = np.sum(sums == 7)

#Estimate the probability
probability = count/num_rolls

print("Total rolls: \n", num_rolls)
print("Number of times sum = 7: \n", count)
print("Estimated probability of getting 7 : \n", probability)