# List

# In contrast with tuples, lists are varible-length and their contents can be modified in-place. We can define them using square brackets [] or using the list type function:

#%%
a_list = [2, 3, 7, None]
tup = 'foo', 'bar', 'baz'
b_list = list(tup)

b_list[1] = 'peekaboo'
b_list # ['foo', 'peekaboo', 'baz']
# %%
# List and tuples are semantically similar (though tuples cannot be modified) and  can be used interchangeably in many functions.

# The list function is frequently used in data processing as a way to materialize an iterator or generator expression:

gen = range(10)
gen # range(10)
# %%
list(gen) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# %%
# Adding and removing elements
# Elements can be appended to the end of the list with append method:

b_list # -> ['foo', 'peekaboo', 'baz']

b_list.append('dwarf') # adding a string to the list

b_list # ['foo', 'peekaboo', 'baz', 'dwarf']
# %%

# Using insert you can insert an element at a specific location in the list:

b_list.insert(1, 'red')

b_list # ['foo', 'red', 'peekaboo', 'baz', 'dwarf']
# %%

# The insertion index must be between 0 and the length of the list, inclusive.

# insert is computationally expensive compared with append, because references to subsequent elements have to be shifted internally to make room for the new element. If you need to insert elements at both the beginning and end of a sequence, you may wish to explore collections.deque, a doble-ended queue, for this purpose.

# Pop
# The inverse operation to insert is pop, which removes and return an element at a particular index:

b_list.pop(2) # returns peekaboo

b_list # ['foo', 'red', 'baz', 'dwarf']
# %%

# Elements can be removed by value with remove, which locates the first such value and removes it from the last:

b_list.remove('foo')
b_list  # ['red', 'peekaboo', 'baz', 'dwarf']

# %%

# If performance is not a concern, by using append and remove, you can use a Python list as a perfectly suitable multiset data structure.

# Check if a list contaisn a value using the (in) keyword:

'Goiaba' in b_list # False
# %%
# COncatenating
a = [1, 2, 3, 4] 
b =  ['a', 'b', 'c', 'd']

c = a + b
c
# %%
# Extend method
c.extend(['I', 'II', 'III', 'IV'])
c #[1, 2, 3, 4, 'a', 'b', 'c', 'd', 'I', 'II', 'III', 'IV']
# %%

kitchen = ['spoon', 'plate', 'fork']
liven_room = ['sofa', 'tv', 'window']
bed_room = ['bed', 'pilow', 'closet']

everything = []

everything.extend([kitchen, liven_room, bed_room])

everything
# %%

# Sorting