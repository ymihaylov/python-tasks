import unittest

import first_solution as solution

COINS = (200, 100, 50, 20, 10, 5, 2, 1)


class CoinsTest(unittest.TestCase):

    def assert_coins(self, money, representation):
        result = {coin: 0 for coin in COINS}
        result.update(representation)

        self.assertEqual(solution.calculate_coins(money), result)

    def test_coins(self):
        self.assert_coins(8.94, {2: 2, 200: 4, 50: 1, 20: 2})

    def test_coins_with_odd_lev(self):
        self.assert_coins(9.94, {2: 2, 200: 4, 100: 1, 50: 1, 20: 2})

    def test_composite_non_prime_coins(self):
        self.assert_coins(0.15, {10: 1, 5: 1})

    def test_composite_prime_coins(self):
        self.assert_coins(0.47, {20: 2, 5: 1, 2: 1})

    def test_all_coins(self):
        self.assert_coins(sum(COINS) / 100, {coin: 1 for coin in COINS})

    def test_no_coins(self):
        self.assert_coins(0.00, {})

    def test_single_coins(self):
        for coin in COINS:
            self.assert_coins(coin / 100, {coin: 1})

    def test_lots_of_money(self):
        self.assert_coins(10000, {200: 5000})

if __name__ == '__main__':
    unittest.main()
