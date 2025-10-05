import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility (optional)
np.random.seed(42)

# Generate synthetic exam scores (Normal distribution)
scores = np.random.normal(loc=70, scale=10, size=100)

# Display basic stats
print("Mean of scores:", np.mean(scores))
print("Standard deviation:", np.std(scores))
print("First 10 scores:", np.round(scores[:10], 2))

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Exam Scores (n=100)")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
