class Arithmetic:
    def __add__(self, other):
        plus = Operator('+', lambda self, other: self + other)
        return Expression(self, plus, other)

    def __sub__(self, other):
        sub = Operator('-', lambda self, other: self - other)
        return Expression(self, sub, other)

    def __mul__(self, other):
        mul = Operator('*', lambda self, other: self * other)
        return Expression(self, mul, other)

    @property
    def variable_names(self):
        return tuple()


class Constant(Arithmetic):
    def __init__(self, value):
        self.value = value

    def evaluate(self, **variables):
        return self.value


class Variable(Arithmetic):
    def __init__(self, name):
        self.name = name

    def evaluate(self, **variable):
        return variable[self.name]

    @property
    def variable_names(self):
        return tuple(self.name,)


class Operator:
    def __init__(self, symbol, function):
        self.symbol = symbol
        self.function = function

    def __str__(self):
        return self.symbol


class Expression(Arithmetic):
    def __init__(self, lhs, operator, rhs):
        self.lhs = lhs
        self.operator = operator
        self.rhs = rhs

    def evaluate(self, **variables):
        return self.operator.function(
            self.lhs.evaluate(**variables),
            self.rhs.evaluate(**variables)
        )

    @property
    def variable_names(self):
        return self.lhs.variable_names + self.rhs.variable_names


def create_constant(value):
    return Constant(value)


def create_variable(name):
    return Variable(name)


def create_operator(symbol, function):
    return Operator(symbol, function)


def create_expression(expression_structure):
    stack = []

    for element in expression_structure:
        if isinstance(element, tuple):
            stack.append(create_expression(element))
        else:
            stack.append(element)

    if len(stack) == 3:
        expression = Expression(stack[0], stack[1], stack[2])
        stack.clear()
        stack.append(expression)

    return stack[0]

six = create_constant(6)
nine = create_constant(9)
times = create_operator('*', lambda lhs, rhs: lhs * rhs)
minus = create_operator('-', lambda lhs, rhs: lhs - rhs)
plus = create_operator('+', lambda lhs, rhs: lhs + rhs)
x = create_variable('x')
y = create_variable('y')

expression = create_expression(
    (six, times, ((x, minus, y), plus, nine))
)

(x + 3 * (y - 2)).evaluate(x=1, y=4)

# print(expression.variable_names)
