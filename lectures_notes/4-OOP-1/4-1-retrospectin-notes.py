def closure(initial):
    def increment_by(x):
        return initial + x

    def decrement_by(x):
        return initial - x

    return increment_by, decrement_by

inc, dec = closure(6)
inc(3)
dec(7)

# ------------


def snitch(init_message):
    def decorator(f):
        print(init_message)

        def snitched(*args, **kwargs):
            print('Called with {}, {}'.format(args, kwargs))
            result = f(*args, **kwargs)
            print('Returned {}'.format(result))

            return result
        return snitched
    return decorator


@snitch('Initializing baba')
def baba(a, b):
    return a / b

# baba(4, 2)
