def is_pangram(sentence):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъьюя'

    unique_letters = sorted(set([
        char.lower() for char
        in sentence if char.isalpha()
    ]))

    return ''.join(unique_letters) == alphabet


# print(is_pangram('Ах, чудна българска земьо, полюшвай цъфтящи жита!'))
is_pangram('Hello World')
