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

# help(sorted)
sort_by(lambda x, y: len(x) - len(y), ['a', 'ab', 'abc'])
