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


# print(is_pangram('Hello World'))
