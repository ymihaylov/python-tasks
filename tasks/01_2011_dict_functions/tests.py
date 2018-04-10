import unittest

import solution

class TestSolution(unittest.TestCase):
    def test_make_multiset_no_duplicates(self):
        self.assertEqual(solution.make_multiset([1, 2]), {1: 1, 2: 1})

    def test_make_multiset_only_duplicates(self):
        self.assertEqual(solution.make_multiset(['spam'] * 42), {'spam': 42})

    def test_make_multiset_with_duplicates(self):
        self.assertEqual(solution.make_multiset(
            ['spam', 'bacon', 'spam', 'spam', 'eggs', 'bacon', 'spam']),
            {'spam': 4, 'bacon': 2, 'eggs': 1})

    def test_ordered_dict_homogeneous_keys(self):
        self.assertEqual(
            solution.ordered_dict({1: 'i', 2: 'ii', 3: 'iii'}),
            [(1, 'i'), (2, 'ii'), (3, 'iii')])

    def test_ordered_dict_heterogeneous_keys(self):
        self.assertEqual(
            solution.ordered_dict({1: 'i', 2.0: 'ii', 2 ** 70: 'wait, what?'}),
            [(1, 'i'), (2.0, 'ii'), (2 ** 70, 'wait, what?')])

    def test_reversed_dict_no_repeating_values(self):
        self.assertEqual(
            solution.reversed_dict({'Nibbler': 3, 'Fillip': 2, 'Turanga': 1}),
            {3: 'Nibbler', 2: 'Fillip', 1: 'Turanga'})

    def test_reversed_dict_repeating_values_only(self):
        value = solution.reversed_dict({'Amy': 2, 'Zapp': 2, 'Kif': 2})[2]
        self.assertTrue(any(_ is value for _ in ['Amy', 'Zapp', 'Kif']))

    def test_reversed_dict_repeating_values(self):
        answer = solution.reversed_dict(
            {'Nibbler': 3, 'Fillip': 2, 'Turanga': 1, 'Amy': 2})

        self.assertEqual(answer[1], 'Turanga')
        self.assertTrue(answer[2] in ['Fillip', 'Amy'])
        self.assertEqual(answer[3], 'Nibbler')

        self.assertTrue(len(answer), 3)

    def test_unique_objects_identical_immutables(self):
        self.assertEqual(
            7, solution.unique_objects([1, 2, 3, 2, 1, 5, 42, None, 'asd']))

    def test_unique_objects_identical_mutables(self):
        empty1, empty2 = [], []
        objects = [empty1, empty2, empty1, empty1, {}, [empty1], [empty1]]

        answer = solution.unique_objects(objects)
        self.assertEqual(answer, 5)

    def test_unique_objects_mutables_and_immutables(self):
        list1, list2 = [1, 2, 3], [1, 2, 3]
        objects = [
            42, list1, list2, list1, list2, {},
            [list2], (list2,), (list2,), 42
        ]
        answer = solution.unique_objects(objects)

        self.assertEqual(answer, 7)


if __name__ == '__main__':
    unittest.main()
