class Constant:
    def __init__(self, value):
        self.value = value

    def evaluate(self, variables):
        # print(variables)
        return self.value


class Variable:
    def __init__(self, name):
        self.name = name

    def evaluate(self, variable):
        return variable[self.name]


class Operator:
    def __init__(self, symbol, function):
        self.symbol = symbol
        self.function = function

    def __str__(self):
        return self.symbol


class Expression:
    def __init__(self, expression_structure):
        self.expression_structure = expression_structure

        self.lhs = expression_structure[0]
        self.operator = expression_structure[1]
        self.rhs = expression_structure[2]

    def get_value_by_object(self, obj, variables):
        if isinstance(obj, Variable):
            return obj.evaluate(variables)
        elif isinstance(obj, Constant):
            return obj.evaluate()

    def evaluate(self, **variables):
        # print(variables)
        # print(self.lhs.evaluate(variables))
        # self.lhs_value = self.get_value_by_object(self.lhs, variables)
        # self.rhs_value = self.get_value_by_object(self.rhs, variables)
        return self.operator.function(
            self.lhs.evaluate(variables),
            self.rhs.evaluate(variables)
        )


def create_constant(value):
    return Constant(value)


def create_variable(name):
    return Variable(name)


def create_operator(symbol, function):
    return Operator(symbol, function)


def create_expression(expression_structure):
    return Expression(expression_structure)


plus = create_operator('+', lambda lhs, rhs: lhs + rhs)
# six = create_constant(6)
six = create_variable('x')
nine = create_constant(9)
expression = create_expression((six, plus, nine))
print(expression.evaluate(x=6))

print(isinstance(six, Variable))
# print(expression.evaluate())

# plus = create_operator('+', lambda lhs, rhs: lhs + rhs)
# x = create_variable('x')
# y = create_variable('y')
# added_expression = create_expression((x, plus, y))
# print(added_expression.evaluate(x=5, y=3))
