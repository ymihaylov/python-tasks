from functools import cmp_to_key


def is_pangram2(sentence):
    alphabet = set('абвгдежзийклмнопрстуфхцчшщъьюя')

    unique_letters = sorted(set([
        char.lower() for char
        in sentence if char.isalpha()
    ]))

    return ''.join(unique_letters) == alphabet


def is_pangram(sentece):
    alphabet = set('абвгдежзийклмнопрстуфхцчшщъьюя')

    return alphabet.issubset(set(sentece.lower()))


def char_histogram(text):
    return {
        char: text.count(char) for char in set(text)
    }


def sort_by(func, arguments):
    return sorted(arguments, key=cmp_to_key(func))


def group_by_type(dictionary):
    result = {}

    for key, value in dictionary.items():
        if (type(key) in result.keys()):
            result[type(key)].update({key: value})
        else:
            result[type(key)] = {key: value}

    return result

print(group_by_type({'a': 12, 'b': 1, 1: "foo"}))
