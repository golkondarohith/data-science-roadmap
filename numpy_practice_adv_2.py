import numpy as np
import matplotlib.pyplot as plt

# Number of steps
n_steps = 1000

# Generate random steps (+1 or -1)
steps = np.random.choice([-1, 1], size=n_steps)

# Compute cumulative sum → position at each step
position = np.cumsum(steps)

# Display first few values
print("First 10 steps:", steps[:10])
print("First 10 positions:", position[:10])

# Plot the random walk
plt.figure(figsize=(10, 5))
plt.plot(position, label='Random Walk', linewidth=2)
plt.title("1D Random Walk Simulation")
plt.xlabel("Step Number")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.show()
