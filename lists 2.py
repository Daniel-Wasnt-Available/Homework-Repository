#-----------------------------------------------------------------------------
# Name:        Lists.py    
# Purpose:     Lists homework
#
# Author:      Daniel
# Created:     25-Sept-2020
# Updated:     27-Sept-2020
#-----------------------------------------------------------------------------

#1 How would you assign the value 'hello' as the third value in a list stored in a variable named spam? 

spam = ['a', 'b', 'hello', 'd']
print(spam)
print()

#2 What does spam[int(int(3 * 2) // 11)] evaluate to?
#a
spam = ['a', 'b', 'c', 'd']
print(spam[int(int(3 * 2) // 11)])
print()

#3 What does spam[-1] evaluate to?
# d
spam = ['a', 'b', 'c', 'd']
print(spam[int(-1)])
print()

#4 What does spam[-6] evaluate to?
# nothing, -6 is not in the range of the list

#5 What does spam[:2] evaluate to?
# it prints the first 2 items in the list
spam = ['a', 'b', 'c', 'd']
print(spam[:2])

#6 What does bacon.index('cat') evaluate to?
# it tells you where cat is seem first in the list
# in this case its the second item so it evalutes to 1

#7 What does bacon.append(99) make the list value in bacon look like?
# it will add 99 to the end of the list
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99)
print(bacon)

#8 What does bacon.remove('cat') make the list value in bacon look like? 
# it removes cat but only the first one, I'm not sure why though and why it doesn't also remove the second cat
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat')
print(bacon)
    
#9 What are the operators for list concatenation and list replication? 
# its the same as strings the operator for list concatenation is +, while the operator for replication is *

#10 What is the difference between the append() and insert() list methods? 
#Both modify an already existing list, but append adds to the end of the list
#whereas insert lets you add an element to a specific spot in the list
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.insert(2,"dog")
print(bacon)

#11 What are two ways to remove values from a list? 
# we can use bacon.remove('11') or del bacon [2]

#12 Name a few ways that list values are similar to string values.
#They have the same operators for concatenation and replication
#They are both used to print
#values and elements in both strings and lists can be changed

#13 Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# They contain references to the list values

#14 What is the difference between copy.copy() and copy.deepcopy()?
#deepcopy() copies original object recursively,
#while shallowcopy() creates a reference object of original object.

#easy comma code
def first(List):
    second = ''.join(List)
    print (second)
    
spam = ['apples,',' oranges,',' banana,',' and ','kiwi']
first(spam)
