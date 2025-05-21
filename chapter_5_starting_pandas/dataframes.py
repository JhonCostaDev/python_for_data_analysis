from import_pandas_Series import divider
import pandas as pd
import numpy as np
'''
# DataFrame
A DataFrame represents a retangular table of data and contains an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dict of Series all sharing the same index. Under the hood, the data is stored as one or more two-dimensional blocks rather than a list, dict, or some other collection of one-dimensional arrays.
'''

# There are many ways to construct a DataFrame, though one of the most common is from a dict of equal-length list or Numpy arrays:

data = {
    'states': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}

df = pd.DataFrame(data)
divider(df)