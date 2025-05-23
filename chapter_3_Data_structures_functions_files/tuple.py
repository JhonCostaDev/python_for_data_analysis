# A tuple is fixed-length, immutable sequence of Python objects.
#%%
tup = 1, 2, 3

type(tup) # (1, 2, 3) -> tuple

# %%
# When you're defining tuples in more complicated expressions, it's often necessary to enclose the values in parantheses, as in this example of creating a tuple of tuples:

nested_tup = (1, 2, 3), (4, 5, 6)
nested_tup

#%%
# We can convert any sequence or iterator to a tuple by invoking tuple:

fruits = ['apple', 'orange', 'lemon']

fruits_tup = tuple(fruits)
fruits_tup 

#%%
language = 'Python'

language = tuple(language)
language

#%%

# Tuples can be accessed with brackets [] as with most other sequence types

language[2]

# PAG 70