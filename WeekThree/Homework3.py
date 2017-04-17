import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

source = 'Classif_Data/wine.csv'
data = pd.read_csv(source)
# drop the column 'color' along axis 1 (0==row, 1==column....other dimensions)
numeric_data = data.drop('color', 1)

# normalize and standardize data

numeric_data_normed = (numeric_data-np.mean(numeric_data, axis=0))
numeric_data_std = (numeric_data_normed/np.std(numeric_data, axis=0))

plt.plot(numeric_data.residual_sugar, "ob", markersize=1)
plt.plot(numeric_data_normed.residual_sugar, "og", markersize=1)
plt.plot(numeric_data_std.residual_sugar, "or", markersize=1)
plt.show()
"""
plt.figure()
plt.subplot(221)
plt.hist(numeric_data.residual_sugar)
plt.subplot(222)
plt.hist(numeric_data_normed.residual_sugar)
plt.subplot(223)
plt.hist(numeric_data_std.residual_sugar)

plt.show()
"""

