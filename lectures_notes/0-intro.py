import sys

print(sys.version)


def real_knights(*knights):
    return ['Sir {}'.format(knight.capitalize()) for knight in knights]


print(real_knights('John', 'snow', 'Rudolf'))
