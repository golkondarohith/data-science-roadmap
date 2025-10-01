import numpy as np

prices = np.array([100, 200, 300])

discount = 10

final_prices = prices - (prices * discount/100)

print(final_prices)
print("\n")

result = final_prices * 2
print(result)