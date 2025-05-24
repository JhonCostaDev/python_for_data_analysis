Chapter 3
# Build-in Data Structes, Functions and Files

This capter discusses capabilities built into the python language that will be uses ubiquitously throughout the book. While add-on libraries like Pandas and Numpy add advanced computational functionality for larger datasets, they are designed to be used together with python's built-in data manipulation tools.

In this chapter, the autor discuss about Python's workhouse data structures:
* Tuples
* Lists
* Dicts
* Sets
* Functions

## Tuple

A tuple is fixed-length, immutable sequence of Python objects.


When you're defining tuples in more complicated expressions, it's often necessary to enclose the values in parantheses, as in this example of creating a tuple of tuples:


We can convert any sequence or iterator to a tuple by invoking tuple:


Tuples can be accessed with brackets [] as with most other sequence types

```python
tup[2] # 3
```

* While the objects stored in a tuple may be mutable themseolves, once the tuple is created it's not possible to modify which object is stored in each slot:
```bash
TypeError                                 Traceback (most recent call last)
Cell In[3], line 4
      1 
      2 mix_tup = tuple(['foo', [1, 2], True])
----> 4 mix_tup[-1] = False

TypeError: 'tuple' object does not support item assignment

```
* If an object inside a tuple is mutable, such as a list, you can modify it in-place:
```python
mix_tup[1].append(3)
mix_tup
```
* We can concatanate tuples using the (+) operator to produce longer tuples:
```python
super_tuple = mix_tup + (6, 0) + ('bar', )
super_tuple
```
* Multiplying a tuple by an integer, as with list, has the effect of concatenating together that many copies of the tuple:
```python
super_tuple * 2
```
* Note that the object themselves are not copied, only the references ot them.


### Unpacking tuples

* If you try to assign to a tuple-like expression of variables, Python will attemp to unpack the value on the righthand side of the equals sign:
```python
a, b, c = tup # a = 1, b = 2, c = 3
```

* Even sequences with nested tuples can be unpacked:
```python
things = ('mouse', 'cellphone', 'keyboard', 'soundbar',(1, 2, 3, 4))

mouse, cellphone, keyboard, soundbar, numbers = things
numbers #(1, 2, 3, 4)
```

* Using this functionality we can easily swap variable names, a task which in many languages might look like:
```java
tmp = a
a = b
b = tmp
```
* But, in Python, the swap can be done like this:
```python
a, b = 1, 2

b, a = a, b

a
```


* A common use of variables unpacking is iterating over sequences of tuples or lists:

```python
seq = [(1,2,3),(4,5,6),(7,8,9)]

for a, b, c in seq:
    print(f'a = {a}, b = {b}, c = {c}')
# output
# a = 1, b = 2, c = 3
# a = 4, b = 5, c = 6
# a = 7, b = 8, c = 9
```

Another common use is returning multiples values from a function. The autor will cover this in more detail later.

*The python language recently acquired some more advanced tuple unpacking to help with situations where we may want to "pluck" a few elements from the beginning of a tuple. This uses the special syntax *rest, which is also used in function signatures to capture an arbitrarily long list of positional arguments:
```python
values = 1, 2, 3, 4, 5

a, b, *rest = values
a # 1
b # 2
rest #[3, 4, 5]
```

* This rest bit sometimes we want to discart; there is nothing special about the rest name. As a matter of convention, many Python programmers will use the underscore(_) for unwanted variables:

```python
values = 1, 2, 3, 4, 5

a, b, *_ = values
a # 1
b # 2
_ #[3, 4, 5]
```

### Tuple methods

* Since the size and sontents of a tuple cannot be modified, it is very light on instance methods. A particularly useful one (also available on list) is count, which counts the number of occurences of a values:
```python
numbers = (1, 2, 2, 2, 3, 4, 5, 2)

numbers.count(2) # 4
```

# List

In contrast with tuples, lists are varible-length and their contents can be modified in-place. We can define them using square brackets [] or using the list type function:

```python
a_list = [2, 3, 7, None]
tup = 'foo', 'bar', 'baz'
b_list = list(tup)

b_list[1] = 'peekaboo'
b_list # ['foo', 'peekaboo', 'baz']
```
List and tuples are semantically similar (though tuples cannot be modified) and  can be used interchangeably in many functions.

* The list function is frequently used in data processing as a way to materialize an iterator or generator expression:
```python
gen = range(10)
gen # range(10)

#Using list method
list(gen) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


### Adding and removing elements
* Elements can be appended to the end of the list with **append** method:
```python
b_list # -> ['foo', 'peekaboo', 'baz']

b_list.append('dwarf') # adding a string to the list

b_list # ['foo', 'peekaboo', 'baz', 'dwarf']

```

### Using insert you can insert an element at a specific location in the list:
```python
b_list.insert(1, 'red')

b_list # ['foo', 'red', 'peekaboo', 'baz', 'dwarf']
```

* The insertion index must be between 0 and the length of the list, inclusive.

#### **insert** is computationally expensive compared with **append**, because references to subsequent elements have to be shifted internally to make room for the new element. If you need to insert elements at both the beginning and end of a sequence, you may wish to explore collections.deque, a doble-ended queue, for this purpose.


## Pop
### The inverse operation to insert is pop, which removes and return an element at a particular index:
```python
b_list.pop(2) # returns peekaboo

b_list # ['foo', 'red', 'baz', 'dwarf']
```

## Remove

* Elements can be removed by value with remove, which locates the first such value and removes it from the last:

```python
b_list.remove('foo')
b_list  # ['red', 'peekaboo', 'baz', 'dwarf']
```

#
If performance is not a concern, by using append and remove, you can use a Python list as a perfectly suitable multiset data structure.

### Check if a list contaisn a value using the (in) keyword:
```python
'Goiaba' in b_list # False
```

The keyword not can be used to negate in:
```python
'Goiaba' not in b_list # True
```

Checking whether a list contains a value is a lot slower than doing so with dicts and sets (to be introduced shortly), as Python makes a linear scan across the values of the list, whereas it can check the others (based on hash tables) in constant time.

## Concatenating and combining lists

Similar to __tuples__, adding two lists together with __+__ concatenates them:
```python
a = [1, 2, 3, 4] 
b =  ['a', 'b', 'c', 'd']

c = a + b
c #[1, 2, 3, 4, 'a', 'b', 'c', 'd']
```
If we have a list already defined, we can append multiple elements to it using the extend method:
```python
c.extend(['I', 'II', 'III', 'IV'])
c #[1, 2, 3, 4, 'a', 'b', 'c', 'd', 'I', 'II', 'III', 'IV']
```

Note that list concatenation by addition is a comparatively expensive operation since a new list must be created and the objects copied over. Using __extend__ to append elements to an existing list, especially if we are building up a large list, is usually preferable. Thus, is faster than the concatenative alternative.