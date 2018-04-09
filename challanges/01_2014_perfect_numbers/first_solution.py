def is_perfect(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    return sum(divisors) == number


print(is_perfect(6))
