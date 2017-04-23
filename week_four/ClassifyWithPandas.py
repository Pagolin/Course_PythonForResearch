"""This case study exemplifies the usage of Pandas library to predict the quality of a whiskey based upon taining dataset correlating flavor to geographical origin etc.
"""
import numpy as np
import pandas as pd

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

print(whisky.tail())

