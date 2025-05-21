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

# Selecting only the first five rows:
divider(df.head())

# Specifying the sequence of columns:

divider(pd.DataFrame(data, columns=['year', 'states', 'pop']))

# If we pass a column that isn't contained in the dict, it will appear with missing values in the result:

df2 = pd.DataFrame(data, columns=['year', 'states', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])

divider(df2)

# A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute:

divider(df2['states'])
divider(df2.year)

'''
Note that the returned Series have the same index as the DataFrame, and theri name attribute has been appropriately set.

Rows can also be retrieved by position or name with the special loc attribute (much more on this later):
'''

divider(df2.loc['three']) # by value

# Retrive information usaing the Iloc

divider(df2.iloc[0]) # By index

# Modifying Columns

# Columns can be modified by assignment.
# For example, the empty 'debt' column could be assigned a scalar value or an array of values:

df2['debt'] = 16.2

divider(df2)

df2['debt'] = np.arange(6.)

divider(df2)

'''
When you are assigning lists or arrays to a column, the value's length must match the length of the DataFrame. If you assign a Series, its labels will be realigned exactly to the DataFrame's index, inserting missing values in any holes: 
'''

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
df2['debt'] = val

divider(df2)

# CREATE A NEW COLUMN

'''
Assigning a column that doesn't exist will create a new column. The del keyword will delete columns as with a dict.

As an exemple of del, I first add a new column of boolean values where the states columns equals 'Ohio':
'''

df2['Eastern'] = df2.states == 'Ohio'

divider(df2)


#Removing a column with del:

del df2['Eastern']

divider(df2)


# Nested dict of dict

pop = {
    'Nevada': {2000: 2.4, 2001: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
}

# If the nested dict is passed to the DataFrame, pandas will interpret the outer dict keys as the columns and the inner keys as the row indices:

df3 = pd.DataFrame(pop)

divider(df3)

# TRANSPOSING

# We can transpose the DataFrame (swap rows and columns) with similar syntax to a Numpy array:

divider(df3.T)

# The keys in the inner dicts are combined and sorted to form the index in the result.

# This isn't true if an explicit index is specified:

divider(pd.DataFrame(pop, index=[2001, 2002, 2003]))
