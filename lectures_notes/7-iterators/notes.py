# What can we iterate?
# - list
# - tuple
# - dict
# - range
# - map and filter objects
# - everything in collections
# - every objects from class that implements __getitem__


### We can iterate thru lazy objects only once
squares = map(lambda x: x ** 2, range(5))
# for number in squares:
#     print(number)
#
# for number in squares:
#     print(number)


### __iter__
# __iter__ returns object-iterator that we can iterate the collection
# Object-Iterator is object that remembers current crawl through collection
# Object that has method next

### __next__
# Returns the next value of collection
# Raise StopIteration Exception, when the collection is in the end

# If a is object-iterator =>
# iter(a) <=> a.__iter__()
# next(a) <=> a.__next__()
# Never use a.__method__() instead of method(a)

### Example
interjections = [
    'Ring-ding-ding-ding-dingeringeding!',
    'Wa-pa-pa-pa-pa-pa-pow!',
    'Hatee-hatee-hatee-ho!',
    'Joff-tchoff-tchoffo-tchoffo-tchoff!'
]

iterator = iter(interjections)  # iterator is <list_iterator>
# iterator is lazy - you cannot iterate second time through it

# while True:
#     try:
#         interjection = next(iterator)
#         print(interjection)
#     except StopIteration:
#         break

# or

# for i in iterator:
#     print(i)

## Who iterate the iterator
iterable = iter([1, 2, 3])
print(iter(iterable) is iterable)