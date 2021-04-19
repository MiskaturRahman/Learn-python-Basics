'''range() – This returns a range object (a type of 
iterable).
xrange() – This function returns the generator 
object that can be used to display numbers only 
by looping. Only particular range is displayed
on demand and hence called “lazy evaluation.'''

import sys
print('hello')

# Python code to demonstrate range() vs xrange()
# on basis of return type

# initializing a with range()
a = range(1, 7)


# testing the type of a
print("The return type of range() is : ")
print(type(a))

# on basis of memory
print('the size alloted using range():')
print(sys.getsizeof(a))

# testing usage of slice operation on range()
# prints without error
print("The list after slicing using range is : ")
print(a[1:3])
