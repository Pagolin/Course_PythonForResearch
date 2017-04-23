import numpy as np
import matplotlib.pyplot as plt

#x is a vector of numbers, randomly drawn from a standard normal distribution by np.random.normal
x = np.random.normal(size=100000)
y = np.random.gamma(2, 3,100000)
"""
create a histogram
normalize it : normed=True
-> showing proportions of obserbservation in stead of absolut count
specify x-scaling: bins= vector_of_x_value_distr e.g. np.linspace(-5,5, 20)
"""
#plt.hist(x, normed=True,bins=np.linspace(-5,5, 21))
#plt.hist(y, bins= 30, cumulative=True)




#create a figure with several plots
plt.figure()
plt.subplot(221)
plt.hist(x, normed=True,bins=30)
plt.subplot(222)
plt.hist(y, bins= 30, cumulative=True)

#show all plt objects created
plt.show()