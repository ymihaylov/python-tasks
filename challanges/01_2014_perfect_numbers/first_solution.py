def is_perfect(number):
    divisors = []
    for i in range(1, number / 2):
        if (number % i == 0):
            divisors.append(i)

    return sum(divisors) == number
