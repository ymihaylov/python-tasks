# Finishing solution
# Check website for more creative solutions


class Arithmetic:
    def __add__(self, other):
        if isinstance(other, int):
            other = Constant(other)

        plus = Operator('+', lambda self, other: self + other)
        return Expression(self, plus, other)

    def __radd__(self, other):
        if isinstance(other, int):
            other = Constant(other)

        plus = Operator('+', lambda self, other: self + other)
        return Expression(self, plus, other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Constant(other)

        sub = Operator('-', lambda self, other: self - other)
        return Expression(self, sub, other)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Constant(other)

        sub = Operator('-', lambda self, other: other - self)
        return Expression(self, sub, other)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Constant(other)

        mul = Operator('*', lambda self, other: self * other)
        return Expression(self, mul, other)

    def __rmul__(self, other):
        if isinstance(other, int):
            other = Constant(other)

        mul = Operator('*', lambda self, other: self * other)
        return Expression(self, mul, other)

    @property
    def variable_names(self):
        return tuple()


class Constant(Arithmetic):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def __str__(self):
        return str(self.value)


class Variable(Arithmetic):
    def __init__(self, name):
        self.name = name

    def evaluate(self, **variable):
        return variable[self.name]

    @property
    def variable_names(self):
        return tuple(self.name,)

    def __str__(self):
        return self.name


class Operator:
    def __init__(self, symbol, func):
        self.symbol = symbol
        self.function = func

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

    def __str__(self):
        return "({0} {1} {2})".format(
            str(self.lhs),
            str(self.operator),
            str(self.rhs)
        )


def create_constant(value):
    return Constant(value)


def create_variable(name):
    return Variable(name)


def create_operator(symbol, func):
    return Operator(symbol, func)


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
