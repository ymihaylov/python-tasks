class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # attributes are accesible only by self. Without implicit scopes.
    def _coords(self):
        return (self.x, self.y, self.z)

    def length(self):
        return sum(_ ** 2 for _ in self._coords()) ** 0.5

    # Mutating method
    def normalize(self):
        length = self.length()

        self.x /= length
        self.y /= length
        self.z /= length

    # Non-mutating method
    def normalized(self):
        length = self.length()

        return Vector(
            self.x / length,
            self.y / length,
            self.z / length
        )

    def __eq__(self, other):
        return self._coords() == other._coords()

v = Vector(1, 4, 6)
# print(v._coords())

# _coords is protected method
# _ is valid name for variable

# Restrictions for protected and private is resposible to programmer

# Methods and attributes that starts with _ are protected
# Methods and attributes that starts with __ are private

##########

# Unbound methods
v1 = Vector(1.0, 2.0, 3.0)
v2 = Vector(1.0, 2.0, 3.0)
v3 = Vector(7.0, 8.0, 9.0)

# print(v1 == v2)

# print(Vector.length(v1))
# print(Vector.length(v2))
# This is useful when:
# print(list(map(Vector.length, [v1, v2, v3])))

#####

# State
# Mutable са обекти, които променят вътрешното си състояние във времето
# Immutable са обекти които никога не променят вътрешнот си състояние
# Повечето обекти в Python са mutable

####

# Equality
# Може да се провери дали два обекта са равни по стойност с ==
# Може да се провери дали две имена сочат към един и същ обект с is
# __eq__ за предефиниране на равенството
# По подразбиране __eq__ е имплементирана с is


####

# Dunder methods (Magic methods)
# __add__(self, other) - self + other
# __sub__(self, other) - self - other
# __mul__(self, other) - self * other
# __truediv__(self, other) - self / other
# __floordiv__(self, other) - self // other
# __mod__(self, other) - self % other
# __lshift__(self, other) - self << other
# __rshift__(self, other) - self >> other
# __and__(self, other) - self & other
# __xor__(self, other) - self ^ other
# __or__(self, other) - self | other

# Cast types
# __int__(self) - int(обект)
# __float__(self) - float(обект)
# __complex__(self) - complex(обект)
# __bool__(self) - bool(обект)

####
# Objects, that can be invoked as a functions

class Stamp:
    def __init__(self, name):
        self.name = name

    def __call__(self, something):
        print("{0} was stamped by {1}".format(something, self.name))

stamp = Stamp("The government")
# stamp("That thing there")


###
# getattr / setattr
# Dynamic set and change attributes
v1 = Vector(1, 1, 1)
getattr(v1, 'y')
setattr(v1, 'z', 5)

###
# Static Methods


class GoatSimulator:
    goats = []

    @staticmethod
    def register(name):
        GoatSimulator.goats.append(name)
        print(len(GoatSimulator.goats), " goats are registered now")

# GoatSimulator.register('esh')
# GoatSimulator.register('presh')
# GoatSimulator.register('zas')
# print(GoatSimulator.goats)

###
# Class methods


class Countable:
    _count = 0

    def __init__(self, data):
        self.data = data
        type(self).increase_count()

    @classmethod
    def increase_count(cls):
        cls._count += 1

    @classmethod
    def decrease_count(cls):
        cls._count -= 1

    def __del__(self):
        type(self).decrease_count()


p = Countable(['hello', 'world'])

####
# Destructor
# Когато даден обект е събран от garbage collector-а, тогава се вика метода
# __del__


###
# Property methods
# Така караме някой метод да се преструва на property


class Goat:
    def __init__(self, name, trait):
        self.name = name
        self.trait = trait

    @property
    def description(self):
        return "{} the {} goat".format(self.name, self.trait)

g = Goat('George', 'Gutsy')
# print(g.description)

###
# Property methods setters


class Color:
    def __init__(self, rgba):
        self._rgba = tuple(rgba)

    @property
    def rgba(self):
        return self._rgba

    @rgba.setter
    def rgba(self, value):
        self._rgba = tuple(value)

red = Color([255, 0, 0])
# print(red.rgba)
red.rgba = [127, 0, 0]
# print(red.rgba)


# Vector 6
def addition(a, b):
    return Vector(a.x + b.x, a.y + b.y, a.z + b.z)


class Vector2:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    __add__ = addition

print(Vector2(1.0, 2.0, 3.0) + Vector2(4.0, 5.0, 6.0))
# Functions are first class objects
# Methods are attributes of the class
# Classes are dymaic
# Self is explicit
