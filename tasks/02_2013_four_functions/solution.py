from collections import defaultdict


def groupby(func, items):
    grouped_items = defaultdict(list)

    for item in items:
        grouped_items[func(item)].append(item)

    return dict(grouped_items)


def iterate(func):
    break

bracketisers = iterate(lambda x: '(' + x + ')')
no_brackets = next(bracketisers)
no_brackets('hello world')
