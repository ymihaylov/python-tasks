import unittest
import my_solution as solution


class PowerOfTwoTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(solution.powers_of_two_remain([]))

    def test_single_number_in_list_should_always_be_true(self):
        self.assertTrue(solution.powers_of_two_remain([8]))
        self.assertTrue(solution.powers_of_two_remain([15]))
        self.assertTrue(solution.powers_of_two_remain([112]))

    def test_multiple_numbers_in_list_true(self):
        self.assertTrue(solution.powers_of_two_remain([7, 8]))
        self.assertTrue(solution.powers_of_two_remain([34, 78, 54]))

    def test_multiple_numbers_in_list_false(self):
        self.assertFalse(solution.powers_of_two_remain([4, 8, 12]))
        self.assertFalse(solution.powers_of_two_remain([8, 16, 24]))

if __name__ == '__main__':
    unittest.main()
