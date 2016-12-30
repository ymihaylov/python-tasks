# For docs
# help(str)

my_var = 'spam'.upper()
# print(my_var, len(my_var), my_var[1])

# Integer doesnt have max size
# print(2 ** 4 ** 8)

# True, False, None
# When function doesnt return anything, it returns None

# print(type(1), type('hello'), type(len))
# Everything is an object and it has class (functions too)
# print(type(type(type)))

# Python is dynamic language. Values has type, but names doesnt.

# Structures
# List
my_list = [1, 2, 3]
# print(my_list)
# Mutable, without fixed lenght
# Guaranteed arrangement
# Heterogeneous - Different types of elements
my_list.append(5)
# print(my_list)
del(my_list[1])
# print(1 in my_list)

# Dict
ages = {'Pesho': 18, 'Gosho': 20}
# print(ages['Gosho'])
# print(ages.get('Stamat', 'Nqma takyv'))
# Not guaranteed arrangment

# Tuple
args = (9.8, 10, 12)
# print(args[2])
# args[1] = 5 # YOU CANNOT DO THAT!
# Its immutable
# Guaranteed arrangement
# Use for return few values from function

# Set
unique_numbers = {2, 3, 4, 5, 5}
# print(unique_numbers) # The second 5 doesnt exist
unique_numbers.add(12)
unique_numbers.remove(5)
# print(unique_numbers)
my_list = [1, 2, 15, 16, 2, 1, 15]
# print(set(my_list))
# Not guaranteed arrangement

# Mutable vs Immutable
# Immutable are values that cannot be change
a = 5
a += 2
# Thats code doesnt change the value. Just a is linked to 7.
# Immutables are int, float, string, tuples, True, False, None
a = [1, 2, 3]
a.append(4)
# This changes the list that is linked to a. Lists are immutable
# As key of dict or elemnt of set may be used only immutable values

# Conditions
# a = 5
# if a == 2:
#     print('Its two!')
# elif a == 5:
#     print('Its five!')
# else:
#     print('Its not two or five')
# Use and, or and not
# False values are: False, None, 0, 0.0, 0j, '', emtpy structures,

# While
a = 10
while a > 5:
    a -= 1
    # print('a is {}'.format(a))

# For
primes = [3, 5, 7, 11]
# for x in primes:
#     print (x ** 2)

people = {'John': 12, 'Snow': 13}
# for name, age in people.items():
#     print('{} is {} years old.'.format(name, age))

# break, continue - only fo innermost loop


# Functions
def multiply(a, b=2):
    return a * b

# print(multiply(5, 10))


def varfunc(some_arg, *args, **kwargs):
    print(some_arg)
    print(args)
    print(kwargs)

varfunc('arg1', 1, 2, 3, name='Bob', age=15)

# args and kwargs names are conventions

# Lambda Functions
# Functions are objects
def baba():
    print('Banica')

def call(function, times):
    for _ in range(times):
        function()

# call(baba, 5)
