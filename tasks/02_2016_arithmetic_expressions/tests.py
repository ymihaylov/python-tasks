import unittest
import solution


class SampleTest(unittest.TestCase):
    def test_literals(self):
        x = solution.create_variable('x')
        y = solution.create_variable('y')

        expression_result = (x + 3 * (y - 2)).evaluate(x=1, y=4)
        self.assertEqual(expression_result, 7)

    def test_five_plus_three(self):
        plus = solution.create_operator('+', lambda lhs, rhs: lhs + rhs)
        x = solution.create_variable('x')
        y = solution.create_variable('y')
        added_expression = solution.create_expression((x, plus, y))
        self.assertEqual(added_expression.evaluate(x=5, y=3), 8)

    def test_operators(self):
        y = solution.create_variable('y')
        twelve = solution.create_constant(12)
        expression = y + twelve
        self.assertEqual(expression.evaluate(y=3), 15)

    def test_variable_names(self):
        x = solution.create_variable('x')
        y = solution.create_variable('y')
        eight = solution.create_constant(8)

        expression = x + y + eight
        self.assertEqual(expression.variable_names, ('x', 'y'))

    def test_complex_expression(self):
        six = solution.create_constant(6)
        nine = solution.create_constant(9)
        times = solution.create_operator('*', lambda lhs, rhs: lhs * rhs)
        minus = solution.create_operator('-', lambda lhs, rhs: lhs - rhs)
        plus = solution.create_operator('+', lambda lhs, rhs: lhs + rhs)
        x = solution.create_variable('x')
        y = solution.create_variable('y')

        expression = solution.create_expression(
            (six, times, ((x, minus, y), plus, nine))
        )

        self.assertEqual(expression.evaluate(x=5, y=2), 72)

    def test_variable_evaluation(self):
        self.assertEqual(solution.create_variable('x').evaluate(x=42), 42)

    def test_constant_evaluation(self):
        self.assertEqual(solution.create_constant(5).evaluate(), 5)
        self.assertEqual(solution.create_constant(10 + 5).evaluate(), 15)

if __name__ == '__main__':
    unittest.main()
