# Lists
# list : offset
# list : Append

## In python, List is a data structure where you can organize and store any datatype.

## If we want to store some group of data which have some sort of connection between them.

## Lists are used to store multiple items in a single variable.

## Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

## syntax: [element1, element2, element3,....], Here the element can be of any data type.

## List follow index data structure hence they are store in order.

## offset: distance between two memory location is known as offset. In the below example.. rose has 0 offset from the beginning of the list, lilly has 1 offset from the beginning of the list, and sunflower has 3 offset from the beginning of the list.

flowers = ["rose", "lily", "sunflower"]
print(flowers)
print(type(flowers))# list

#* To fetch the element from the list using offset or index
print(flowers[2])

#* Index error: list index out of range, if the index doesn't exist
# print(flowers[3])

#* To fetch the element from the list using offset or index based on negative value
print(flowers[-1])

#* Updating the list element
flowers[-1] = "marigold"

print(flowers)


#* append(): adding a new element in the existing list
# "append" will add single element at a time at the end of the list
# manipulate the original list
flowers.append('sunflower')
print(flowers)


#* extend() to add a new list/ multiple items as an elements inside existing list
# manipulate the original list
flower2 = ['carnation','jasmine','daisy']
flowers.extend(flower2)

print(flowers)
'''
The list data type has some more methods. Here are all of the methods of list objects:


list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
'''