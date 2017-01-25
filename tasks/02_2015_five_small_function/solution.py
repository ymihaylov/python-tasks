# Extract type

symbols = [('f', 1), (5, 10), ('i', 1), (0.3, 100),
           ('z', 2), ('bu', 1), ('z', 2)]


def extract_type(symbols, type):
    result = ''

    for pair in symbols:
        if isinstance(pair[0], type):
            result += str(pair[0]) * pair[1]

    return result


def extract_type2(symbols, type):
    valid_pairs = [
        pair for pair
        in symbols
        if isinstance(pair[0], type)]

    return ''.join([
        pair[1] * str(pair[0]) for pair
        in valid_pairs
    ])


# Reversed dict
def reversed_dict(normal_dict):
    # return dict((value, key) for (key, value) in normal_dict.items())
    # return(dict(zip(dict_for_reverse.values(), dict_for_reverse.keys())))
    return dict(map(reversed, normal_dict.items()))


# reps
def reps(numbers):
    return tuple([
        number for number
        in numbers
        if numbers.count(number) > 1
    ])
