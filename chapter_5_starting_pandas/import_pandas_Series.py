import pandas as pd
import numpy as np

def divider(obj) -> None:
    '''Just to shows a divider in the console outputs between the lines'''
    print('=================================')
    print(obj)
    print('=================================')
# While pandas adopts many coding idioms from NumPy, the biggest difference id that Pandas is designed for working with tabular or heterogeneous data. NumPy, by contrast, is best suited for working with homogeneous numerical array data.

# Series
# A Series is a one-dimensional array-like object containing a sequence of values and an associated array of data labels, called its index.

obj = pd.Series([4, 7, -5, 3])

divider(obj)

# The string representation of a Series displayed interactively shows the index on the left and the values on the right. Since we did not specify an index for the data, a default one consisting of the integers 0 through N -1 (where N is the length of the data) is created
divider(obj.values)
divider(obj.index)
divider

# Create a Series with an index identifying each data point with a label:

obj2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
divider(obj2)


# Like a Numpy arrays, we can use labels in the index when selecting single values or a set of values:

divider(obj2['c'])
divider
obj2['d'] = 80


divider(obj2['d'])


# show through the index
divider(obj2[['a','d']])


# Using Numpy functions or Numpy-like operations, such as filtering with a boolean array, scalar multiplication, or applying math functions, will preserve the index-value link:


divider(obj2 > 0)


divider(obj2[obj2 > 0])


divider(obj2[obj2 < 0])



divider(obj2* 4)


divider(np.exp(obj2))


# Another way to think about a Series is as a fixed-length, ordered dict, as it is a mapping of index values to data values. It can be used in many context where you might use a dict:

divider('b' in obj2)


divider('e' in obj2)


# should you have data contained in a Python dict, you can create a Series from it by passing the dict:

dict_data = {
    'Ohio': 35000,
    'Texas': 71000,
    'Oregon': 16000,
    'Utah': 5000
}

obj3 = pd.Series(dict_data)

divider(obj3)

# When we are only passing a dict, the index i the resulting Series will have the dict's keys in sorted order. We can override this by passing the dict keys in the order we want them to appear in the resulting Series:

states_ordered = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(dict_data, index=states_ordered)

divider(obj4)

# Here, three values found in dict_data were places in the appropriate locations, but since no value for 'California' was found, it appears as NaN (Not a Number), which is condidered in Pandas to mark missing or NA values. Since 'Utah' was not included in states, it is excluded from the result object.

# The autor will  use the terms 'missing' or 'NA' interchangeably to refer to missing data. The isnull and notnull functions in Pandas should be used to detect missing data:

divider(pd.isnull(obj4))

divider(pd.notnull(obj4))

divider(obj4.isnull())

# A useful Series feature for many applications is that it automatically aligns by index label in arithmetic operations:

obj5 = obj3 + obj4

divider(obj5)

## Name attribute
# Both the \Series object itself and its index have a name attribute, which integrates with other keys areas of pandas functionality:

obj5.name = 'Population'
obj5.index.name = 'States'

divider(obj5)

# Object index can be altered in -place assignment:
obj.index = ['bob', 'steve', 'jeff', 'ryan']
divider(obj)
