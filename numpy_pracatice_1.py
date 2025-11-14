import numpy as np

random_integers = np.random.randint(1, 101, size=20)
print(random_integers)

random_integers1 = np.random.choice(np.arange(1, 101), size=20, replace=False) 
print(random_integers1)

print(type(random_integers))