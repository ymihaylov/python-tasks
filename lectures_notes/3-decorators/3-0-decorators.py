# Functions are objects that have method call

# One variable dies with the scope that lives in it

# Arguments
# Positioned or Named
# After named, we cant add positioned
# Arguments go to locals


# Nested functions
def outer(x):
    print(x)

    def inner():
        x = 0
        print(x)

    inner()

    print(x)

# outer(5) # 5, 0, 5

# https://docs.python.org/3/reference/executionmodel.html#naming-and-binding

# Functions are first-class objects


# In functions we have closures
def start(x):
    def increment(y):
        return x + y

    return increment

first_inc = start(0)
second_inc = start(8)

first_inc(3)
second_inc(3)

first_inc(1)
second_inc(2)


# One serios problem
def spam(n):
    spams = ('spam', ) * (n - 1)

    return 'I would like {} and spam'.format(", ".join(spams))


def eggs(n):
    return 'I would like {} eggs'.format(n)


def served_by(func, server):
    def cached_server(n):
        return '{}, dear {}'.format(func(n), server)

    return cached_server

# eggs = served_by(eggs, 'sir')
# spam = served_by(spam, 'madam')


# Lets thanks
def thank_you(func):
    def with_thanks(n):
        return '{}. Thank you very much!'.format(func(n))
    return with_thanks


spam = thank_you(served_by(spam, 'sir'))
# print(spam(5))
# Its very complex
#################


def fibonacci_old(x):
    if x in [0, 1]:
        return 1

    return fibonacci(x - 1) + fibonacci(x - 2)


# Recursive version of fibonacci is very very slow
# We can calculate every result only once

# f(function) -> function

# First example of decorators
def memorize(func):
    memory = {}

    def memorized(*args):
        if args in memory:
            return memory[args]

        result = func(*args)
        memory[args] = result

        return result

    return memorized


@memorize
def fibonacci(x):
    if x in [0, 1]:
        return 1

    return fibonacci(x - 1) + fibonacci(x - 2)


# fibonacci = memorize(fibonacci)
# print(fibonacci(5))

# Second Example of decorators
def notifyme(f):

    def logged(*args, **kwargs):
        print(f.__name__, ' called with', args, 'and', kwargs)

        return f(*args, **kwargs)

    return logged


@notifyme
def square(x):
    return x * x

# its same like
# square = notifyme(square)
