import math

foods = ['spam', 'eggs', 'ham']
things = foods
things[1] = 'chips'
# print(foods[1]) # prints chips

my_list = '12 34 16'.split() + [(False, False)]
my_dict = dict(my_list)
# print(my_list)
# print(my_dict[0])

# In python every collection is iterable

cute_animals = ['cat', 'raccoon', 'panda', 'red panda', 'marmot']
# print(cute_animals[1])
# print(cute_animals[-1])
# print(cute_animals[1:3]) # ['racoon', 'panda']
# print(cute_animals[1:-1])
# print(cute_animals[::-1]) # reverse
# print(cute_animals[-1:0:-1])
# print(cute_animals[-1:0:-2])

# is vs ==
# lists contains pointer to elements

# Methods
cute_animals.index('raccoon')
cute_animals.count('raccoon')
cute_animals.append('raccoon')
cute_animals.count('raccoon')
cute_animals.extend(['panda', 'manda']) # like + but its faster
cute_animals.sort()

# range - iterable
range(3)
range(10, 15)
range(13, 0, -1)

# Tuples
# Tuples cannot be change, but can change inner structures
# (if the element is array)
people = 'Niki', 'Pesho', 'Gosho' # tuple
people = ('Niki') # people is string 'Niki'

numbers = (1, 2, 3)
a, b, c = numbers

a, *b, c = 1, 2, 3, 4, 5 # b is list

# Compare tuple lexicaly

# Sets
# {} is not empty set
# Operations with sets like math

# Dict
dict(france="Paris", italy="Rome")
dict([('One', 'I'), ('Two', 'II')])
dict.fromkeys([1, 2, 3], 'Unknown')

data = [('John', 'Tilsit'), ('Eric', 'Cheshire'), ('Michael', 'Camembert'),
        ('Terry', 'Gouda'), ('Terry', 'Port Salut'), ('Michael', 'Edam'),
        ('Eric', 'Ilchester'), ('John', 'Fynbo')]

def cheeses_by_owner(cheeses_data):
    by_owner = {}
    for owner, cheese in cheeses_data: # <- tuple unpacking; same as (o, c)
        if owner in by_owner:
            by_owner[owner].append(cheese)
        else:
            by_owner[owner] = [cheese]

    return by_owner

# print(cheeses_by_owner(data))

# map/filter/reduce/all/any
# map and filter are lazy

# Comprehesion
# print([x * x for x in range(0, 10)])
# print([x * x for x in range(0, 10) if x % 2])
# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# Generator expression
# () instead of {}
# Lazy evaluation
# On every step iterator

# Set comprehension
# print({int(math.sqrt(x)) for x in range(1, 100)})

# Dict comprehension
# print({i: chr(65+i) for i in range(10)})

# Other collections
# deque - two way queue
# OrderedDict
# defaultdict - default values
# Counter - dict that counts repated values
# namedtuple
