def count_of_spam(number):
    count = 0

    while number % 3 == 0:
        count += 1
        number //= 3

    return count


def prepare_meal(number):
    count = count_of_spam(number)
    meal = (count * 'spam ').strip()

    if (number % 5 == 0):
        if (meal == ''):
            meal = 'eggs'
        else:
            meal += ' and eggs'

    return meal

