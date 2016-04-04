import itertools
print(dir(itertools))
# help(itertools)
quit()
# We can iterate 
# lists
# set
# tuple
# dict
# range
# map and filter
# collections
# Every class that implement __getitem__

squares = map(lambda x: x ** 2, range(5))

for number in squares:
    print(number)
# 0 1 4 9 16 

for number in squares:
    print(number)
#

# ---
# __iter__ - returns object-iterator. 
# Iterator is an object that that keep current position (object that have __next__ method)

# __next__ raise StopIteration when 


# ---
interjections = [
    'Ring-ding-ding-ding-dingeringeding!',
    'Wa-pa-pa-pa-pa-pa-pow!',
    'Hatee-hatee-hatee-ho!',
    'Joff-tchoff-tchoffo-tchoffo-tchoff!'
]
iterator = iter(interjections)
while True:
    try:
        interjection = next(iterator)
        print(interjection)
    except StopIteration:
        break

# ---
class IterableThingie:
    def __getitem__(self, index):
        if index < 10:
            return index * 2
        else:
            raise StopIteration()

    def __iter__(self):
    	return iter('12345')

it = IterableThingie()
for i in it:
    print(i)

# --
# odd = filter(lambda num: num % 2, range(10))
# print(iter(odd) is odd)

# ---

loud_names = ['JEFF', 'STONE', 'MIKE', 'EDDIE', 'MATT']
quiet_names = map(lambda name: name.lower(), loud_names)
loud_names[3] = 'VEDDER'
print(list(quiet_names))

# ---

def actors_generator():
    yield 'Graham Chapman'
    yield 'John Cleese'
    yield 'Terry Gilliam'
    yield 'Eric Idle'
    yield 'Terry Jones'
    yield 'Michael Palin'

actors = actors_generator()
for actor in actors:
    print(actor + ' as seen on British TV')

 # ---
class SquaresUpTo:
    def __init__(self, up_to):
        self.up_to = up_to
        self.num = 0

    def __iter__(self):
        return self

    def next(self):
        if self.num > self.up_to:
            raise StopIteration

        square = self.num ** 2
        self.num += 1
        return square

squares = SquaresUpTo(100)

# for square in squares:
    # print(square)

def squares_up_to(number):
    value = 0

    while value <= number:
        yield value ** 2
        value += 1

    raise StopIteration