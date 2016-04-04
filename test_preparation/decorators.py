# Funcitons are objects but have method __call__

global_one = 1

def foo():
    local_one = 2
    print(locals())

print(locals() == globals())

# ---

# One variable die when the scope die

# ---
# Funciton arguments can be passed as named or positions
def test(arg1, arg2, calcSum=True, *dict):
	print(dict)

# test(1, 2, 3, {'hll': 1})

# ---
def outer(x):
    print(x)

    def inner():
        x = 0
        print(x)

    inner()
    print(x)

# outer(5)

# inner goes to locals for outer
# nonlocal - dont use it

# ---
# Functions are first class objects - can be arguments of function, return from function, collection with functions, can be assigned as function

# ---

def start(x):
    def increment(y):
        return x + y
    return increment

first_inc  = start(0)
second_inc = start(8)

print(first_inc(3))
print(second_inc(3))

first_inc(1)
second_inc(2)

# ---
def served_by(server):
	def decorator(func):
		def cached_server(n):
			return "{}, dear {}".format(func(n), server)
		return cached_server
	return decorator


def thank_you(func):
	def with_thanks(n):
		return "{}. Thank you very much!".format(func(n))
	return with_thanks

@served_by('sir')
def spam(n):
    spams = ("spam", ) * (n - 1)
    return "I would like {} and spam".format(", ".join(spams))

@thank_you
@served_by('sir')
def eggs(n):
    return "I would like {} eggs.".format(n)

eggs(5)
# eggs = thank_you(served_by(eggs, "sir"))
# spam = served_by(spam(4), 'madam')
print(eggs(5))

# ---

def fibonacci(x):
    if x in [0,1]:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(5))


# ---
def memorize(func):
    memory = {}
    
    def memorized(*args):
        if args in memory:
            return memory[args]

        result = func(*args)
        memory[args] = result

        return result
    return memorized

fibonacci = memorize(fibonacci)
print(fibonacci(5))

# ---
@memorize
def fibonacci(x):
    if x in [0,1]:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

# ---
def notifyme(f):
    def logged(*args, **kwargs):
        print(f.__name__, ' called with', args, 'and', kwargs)
        
        return f(*args, **kwargs)

    return logged

@notifyme
def square(x):
    return x * x

res = square(25) # 625
#square was called with (25,) and {}.

# ---
def work(): pass
work = notifyme(work)
work = staticmethod(work)
work = staticmethod(notifyme(work))

# ---
def accepts(*types):
    def accepter(f):
        def decorated(*args):
            for (i, (arg, t)) in enumerate(zip(args, types)):
                if not isinstance(arg, t):
                    raise TypeError(
                        """Argument #{0} of '{1}' is not {2}""".format(
                            i,
                            f.__name__,
                            t.__name__))
            #TODO: more complex checks
            return f(*args)
        return decorated
    return accepter

@accepts(int, int)
def add(a, b):
    return a+b