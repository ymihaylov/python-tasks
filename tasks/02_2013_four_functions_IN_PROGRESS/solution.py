from collections import defaultdict
from itertools import count


def groupby(func, items):
    grouped_items = defaultdict(list)

    for item in items:
        grouped_items[func(item)].append(item)

    return dict(grouped_items)


def double(x):
    return 2 * x


def iterate(func):
    def composer(n):
        return lambda x: func(composer(n - 1)(x)) if n > 0 else x

    return (composer(n) for n in count())


# i = iterate(double)

# print(i)
# f(3)  # 3

# f = next(i)
# f(3)  # 6

# f = next(i)
# f(3)  # 12

# bracketisers = iterate(lambda x: '(' + x + ')')
# no_brackets = next(bracketisers)
# no_brackets('hello world')
