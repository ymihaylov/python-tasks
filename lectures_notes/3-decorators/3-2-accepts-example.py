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

            return f(*args)
        return decorated

    return accepter


@accepts(int, int)
def multiply(x, y):
    return x * y

multiply(5, 'dsadsa')
