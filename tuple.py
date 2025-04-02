
'''Tuples are ordered collections of data items.

They store multiple items in a single variable.

Tuple items are separated by commas and enclosed in round brackets ( ).

Tuples are immutable, meaning they cannot be changed after creation.'''
tup=(1,)
print(type(tup),tup)
xyz=(1,2,3,4,5)
print(len(xyz)-xyz[-1])
animals=("lion","cat","dog","zebra","monkey","rabbit")
if "lion" in animals:
    print("yes")
#nameoftuple[start:end:jumpindex]
# this statement create a new tuple
print(animals[0:4:2])
#method of tuples:
#count():
#Returns the number of times a specific element appears in the tuple.
my_tuple = (1, 2, 3, 1, 4, 1)
print(my_tuple.count(1))
#index():
#Returns the index of the first occurrence of a specified element in the tuple.
#If the element is not found, it raises a ValueError.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple.index(30)) 




