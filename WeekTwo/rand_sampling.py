import random
import matplotlib.pyplot as plt
import numpy as np


def roll():
    return random.choice(range(1,7))

rolls = [roll() for i in range(100000)]
rollSum10 = [sum([roll() for i in range (10)]) for j in range(10000)]
# Central Limit Thereom: Sums of values of randomly distributed variables will allways approximate normal distribution
row= 3
col= 4
np.random.random((row,col)) # returns array[row][col] of random points of 0 to 1 uniform distribution
mean= 0
standardDev= 1
np.random.normal(mean, standardDev, (row, col))

#alternative way to roll() -> NUMPY is much FASTER than standard python realisation
Rolls= np.random.randint(1,7,(row,col))


plt.hist(rollSum10)
plt.show()