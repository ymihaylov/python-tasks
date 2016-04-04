arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# ---

cute_animals = ['cat', 'raccoon', 'panda', 'red panda', 'marmot']

print(cute_animals[::-1]) # reverse
print(cute_animals[1:3]) # panda only
print(cute_animals[1:-1])
print(cute_animals[-1:0:-2])

quit()

# ---

a, b, c = 'a1', 'b1', 'c1'

print(a, b, c)

# ---

arr1.append(1)
arr1.extend([1, 3])
print(arr1)

# ---

numbers = range(13, 0, -1)

# for number in numbers:
    # print('We can count to ' + str(number))

# --

# Tuple - permanent staff
animals = ('dog', 'cat')
print(animals[0])

# animals[0] = 'fish' # You cant do that!

# ---
animals = 'dog', 'cat', 'dog'
print(animals.count('dog'))
print(animals.index('dog'))

# --

people = 'Niki',
print(people) # ('Niki', )
people = ('Niki')
print(people) # returns only string Niki

# ---
numbers = (1, 2, 3)
a, b, c = numbers

# ---
# a, *b, c = 1, 2, 3, 4, 5, 6
print(b)

# ---
# Lexicography comparasion
print((12, 13) > (11, 12))

# ---
# Set add
numbers = set()
numbers.add(1)
numbers.add(2)

print(numbers)
print(2 in numbers)

favorites_numbers = {7, 10, 5}
print (favorites_numbers)

# | - ob
# & - s

# sets are not ordered

# ---
# {} - is empty dict

# Creating
dict(france='paris', bulgaria='sofia')
print(dict([('One', 'I'), ('Two', 'II')]))
print(dict.fromkeys([1, 2, 3], 'Unkown'))

# If two elements have exact values, then they have the same hash
# Keys must be compered by ==
# Keys must be immutable

# ---
# data = [('John', 'Tilsit'), ('Eric', 'Cheshire'), ('Michael', 'Camembert'),
#         ('Terry', 'Gouda'), ('Terry', 'Port Salut'), ('Michael', 'Edam'),
#         ('Eric', 'Ilchester'), ('John', 'Fynbo')]
# for (owner, cheese) in cheeses_data: # <- tuple unpacking

# ---
# map and filter are lazy
# map filter, reduce, any, all, filter


# ---
# Comprehesions
print([x * x for x in range(0, 5) if x % 2])
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# ---
# Generators
# Like Comprehesions but its with () and its dynamic (lazy evaluation)

# ---
# Set
#  {int(math.sqrt(x)) for x in range(1,100)}
# Dict
# {i: chr(65+i) for i in range(10)}

# --
# defaultdict - Values by default
# can use something['owener'] without check

