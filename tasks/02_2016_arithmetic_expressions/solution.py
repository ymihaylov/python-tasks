class Constant:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class Variable:
    def __init__(self, name):
        self.name = name

    def evaluate(self, **variables):
        return variables[self.name]


class Operator:
    def __init__(self, symbol, function):
        self.symbol = symbol
        self.function = function

    def evaluate():
        pass

    def __str__(self):
        return self.symbol


class Expression:
    def __init__(self, expression_structure):
        self.expression_structure = expression_structure

        self.lhs = expression_structure[0]
        self.operator = expression_structure[1]
        self.rhs = expression_structure[2]

    def evaluate(self, **variables):
        return self.operator.function(
            self.lhs.evaluate(),
            self.rhs.evaluate()
        )

    # def evaluate(self, **variables):
    #     return self.operator.function(
    #         variables[self.lhs.name],
    #         variables[self.rhs.name]
    #     )


def create_constant(value):
    return Constant(value)


def create_variable(name):
    return Variable(name)


def create_operator(symbol, function):
    return Operator(symbol, function)


def create_expression(expression_structure):
    return Expression(expression_structure)


plus = create_operator('+', lambda lhs, rhs: lhs + rhs)
minus = create_operator('-', lambda lhs, rhs: lhs - rhs)
times = create_operator('*', lambda lhs, rhs: lhs * rhs)
six = create_constant(6)
nine = create_constant(9)
expression = create_expression((six, times, nine))

print(expression.evaluate())
# plus = create_operator('+', lambda lhs, rhs: lhs + rhs)
# x = create_variable('x')
# y = create_variable('y')
# added_expression = create_expression((x, plus, y))
# print(added_expression.evaluate(x=5, y=3))
