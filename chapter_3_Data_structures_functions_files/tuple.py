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

# While the objects stored in a tuple may be mutable themseolves, once the tuple is created it's not possible to modify which object is stored in each slot:

#%%
mix_tup = tuple(['foo', [1, 2], True])

mix_tup[-1] = False


# %%

# If an object inside a tuple is mutable, such as a list, you can modify it in-place:

mix_tup[1].append(3)
mix_tup
# %%

# We can concatanate tuples using the (+) operator to produce longer tuples:

super_tuple = mix_tup + (6, 0) + ('bar', )
super_tuple
# %%

# Multiplying a tuple by an integer, as with list, has the effect of concatenating together that many copies of the tuple:

super_tuple * 2

# Note that the object themselves are not copied, only the references ot them.

# %%

# If you try to assign to a tuple-like expression of variables, Python will attemp to unpack the value on the righthand side of the equals sign:

a, b, c = tup
a
# %%

# Even sequences with nested tuples can be unpacked:

things = ('mouse', 'cellphone', 'keyboard', 'soundbar',(1, 2, 3, 4))

mouse, cellphone, keyboard, soundbar, numbers = things
numbers
mouse

# %%

# Using this functionality we can easily swap variable names, a task which in many languages might look like:

tmp = a
a = b
b = tmp

# But, in Python, the swap can be done like this:

a, b = 1, 2

b, a = a, b

a
# %%

# A common use of variables unpacking is iterating over sequences of tuples or lists:

seq = [(1,2,3),(4,5,6),(7,8,9)]

for a, b, c in seq:
    print(f'a = {a}, b = {b}, c = {c}')


# %%

# Another common use is returning multiples values from a function. The autor will cover this in more detail later.

# The python language recently acquired some more advanced tuple unpacking to help with situations where we may want to "pluck" a few elements from the beginning of a tuple. This uses the special syntax *rest, which is also used in function signatures to capture an arbitrarily long list of positional arguments:

values = 1, 2, 3, 4, 5

a, b, *rest = values
a # 1
b # 2
rest #[3, 4, 5]

# This rest bit sometimes we want to discart; there is nothing special about the rest name. As a matter of convention, many Python programmers will use the underscore(_) for unwanted variables:

values = 1, 2, 3, 4, 5

a, b, *_ = values
a # 1
b # 2
_ #[3, 4, 5]


### Tuple methods

# Since the size and sontents of a tuple cannot be modified, it is very light on instance methods. A particularly useful one (also available on list) is count, which counts the number of occurences of a values:

numbers = (1, 2, 2, 2, 3, 4, 5, 2)

numbers.count(2) # 4
# %%
