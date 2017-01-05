import unittest
from first_solution import prepare_meal


class FirstHomeworkTests(unittest.TestCase):

    def test_no_spam_or_eggs(self):
        self.assertEqual('', prepare_meal(11))

    def test_one_spam(self):
        self.assertEqual('spam', prepare_meal(3))

    def test_some_spams(self):
        self.assertEqual('spam spam spam spam', prepare_meal(81))

    def test_some_spams_with_additional_multipliers(self):
        self.assertEqual('spam spam spam spam', prepare_meal(81 * 2 * 7 * 11))

    def test_eggs(self):
        self.assertEqual('eggs', prepare_meal(5))

    def test_eggs_with_additional_egg_multipliers(self):
        self.assertEqual('eggs', prepare_meal(5**4))

    def test_eggs_with_additional_nonegg_multipliers(self):
        self.assertEqual('eggs', prepare_meal(5 * 7 * 11))

    def test_spam_and_eggs(self):
        self.assertEqual('spam and eggs', prepare_meal(15))

    def test_some_spam_and_eggs(self):
        self.assertEqual('spam spam and eggs', prepare_meal(45))

    def test_spam_and_eggs_with_additional_multipliers(self):
        self.assertEqual('spam spam and eggs', prepare_meal(45 * 8 * 7))


if __name__ == '__main__':
    unittest.main()
