"""This case study exemplifies the usage of Pandas library to predict the quality of a whiskey based upon taining dataset correlating flavor to geographical origin etc.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""pd Series and DataFrame are 1D and 2D data arrays with metadata
Series are most commonly constructed from dictionaries, while DataFrames can be constructed from dictionaries of lists
Arithmetic operations on both are carried out index based, i.e. setting custom index allows for arithmetic operation an non-sorted structures where non-matching indices will lead to NAN"""


data = {'letters' : ['A', 'B', 'C'],
        'numbers' : [12, 13, 14],
        'monties' : ['John', 'Eric', 'Michael']}
ind = ["Spam", "Spam and eggs", "Spam, Spam and eggs"]
series_example = pd.Series([1,2,3], index=ind)
dataframe_example = pd.DataFrame(data, columns=['letters', 'numbers', 'monties'], index=ind)
print(series_example, dataframe_example, dataframe_example.numbers + series_example)

#getting wiskey data
whisky = pd.read_csv("./whisky_data/whiskies.txt")
#add column Region
whisky["Region"] = pd.read_csv("./whisky_data/regions.txt")

#Estimating pearson correlation (linear correlation coefficient ) in our data
#whisky.columns  => Index(['RowID', 'Distillery', 'Body', 'Sweetness', 'Smoky', 'Medicinal','Tobacco', 'Honey', 'Spicy', 'Winey', 'Nutty', 'Malty', 'Fruity','Floral', 'Postcode', ' Latitude', ' Longitude', 'Region'], dtype='object')

#Dataframe containing all rows for columns with "flavor-data"
flavors = whisky.iloc[:, 2:14]

#Get the pearson correlation among flavors
corr_flavors = pd.DataFrame.corr(flavors)

plt.figure(figsize=(10, 10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("flavor_correlation.pdf")

#get the correlation among whiskies
corr_whisky = pd.DataFrame.corr(flavors.transpose())

plt.figure(figsize=(10, 10))
plt.pcolor(corr_whisky)
plt.axis("tight") #Limit axis to available data, i.e. no white spaces at axis ends
plt.colorbar()
plt.savefig("whisky_correlation.pdf")

"""Spectral co-clustering 
-> finding corresponding clusters in related data i.e. sets of words occureíng together in particulsr sets of tests
-> simultaneously clustering rows and columns of a matrix
e.g. find co-clustering properties for the six regional clusters the whiskies come from
"""
from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0) #create the moel object
model.fit(corr_whisky)
whiskies_per_region = np.sum(model.rows_, axis=1) #observation per cluster
regions_per_whisky = np.sum(model.rows_, axis=0) #clusters per observation
print(whiskies_per_region)
print(regions_per_whisky)