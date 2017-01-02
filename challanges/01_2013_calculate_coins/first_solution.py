COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def calculate_coins(price):
    price = round(price * 100)
    change = {}

    for coin in COINS:
        count = int(price / coin)
        change[coin] = count
        price = price - (count * coin)

    return change
