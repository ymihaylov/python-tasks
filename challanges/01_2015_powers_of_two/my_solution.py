import math


def powers_of_two_remain(numbers):
    powers = []

    for number in numbers:
        powers.extend(max_powers_of_two(number))

    odds = ([
        number for number in powers
        if powers.count(number) % 2 != 0
    ])

    return bool(odds)


def max_powers_of_two(number):
    numbers = []
    for i in range(number, 0, -1):
        log_of_two = math.log(i, 2)
        new_sum = sum(numbers) + i

        if log_of_two.is_integer() and new_sum <= number:
            numbers.append(i)

    return numbers

