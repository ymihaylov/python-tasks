from functools import cmp_to_key
from collections import defaultdict


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
    result = defaultdict(dict)

    for key, value in dictionary.items():
        result[type(key)].update({key: value})

    return result


def anagrams(string_list):
    pass
