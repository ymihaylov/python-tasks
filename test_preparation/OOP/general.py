import math

# Everything is an object
# Object are open
# Classes are open
print(type(42))
print(type([]))


# Always first argument is self - object that is treated
# Attributes dont require declaration
# Constructor is initializator

# _var - protected
# __var - private

# mutable vs immutable
# Most objects in python are mutable
def addition(a, b):
    return Vector(a.x + b.x, a.y + b.y, a.z + b.z)

class Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	__add__ = addition

	# protected method
	def _coords(self):
		return (self.x, self.y, self.z)

	def length(self):
		return sum(_ ** 2 for _ in self._coords()) ** 0.5

	# Mutating
	def normalize(self):
		length = self.length()
		self.x /= length
		self.y /= length
		self.z /= length

	# Not mutating
	def normalized(self):
		length = self.length()
		return Vector(self.x / length, self.y / length, self.z / length)

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1.length())
print(Vector.length(v1))
print(list(map(Vector.length, [v1, v2, v3])))
print((Vector(1.0, 2.0, 3.0) + Vector(4.0, 5.0, 6.0)).x)

# == - check two object are equal by values
# is - check if two obects are points to the same object
# __eq__ - predefine ==

# Dunder methods (doble under)
# __add__(self, other)
# __sub__(self, other)
# ....
# __int__(self)
# __call__

# ---
#getattr(v1, 'y')
#setattr(v1, 'y', 1)

class GoatSimulator:
    goats = []

    @staticmethod
    def register(name):
        GoatSimulator.goats.append(name)
        print("{} goats are registered now".format(len(GoatSimulator.goats)))

GoatSimulator.register("George the Gutsy Goat")
GoatSimulator.register("Pip the Happy Goat")


# ---
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
    	# Close files, network ports etc.
    	type(self).decrease_count()
    	pass

# First argument of class method is cls


# ---
class Goat:
    def __init__(self, name, trait):
        self.name = name
        self.trait = trait

    @property
    def description(self):
        return "{} the {} goat".format(self.name, self.trait)

g = Goat('Pesho', 'Gutsi')
print(g.description)

# ---
class Color:
    def __init__(self, rgba):
        self._rgba = tuple(rgba)

    @property
    def rgba(self):
        return self._rgba

    @rgba.setter
    def rgba(self, value):
        self._rgba = tuple(value)

red = Color([255,0,0])
print(red.rgba)
red.rgba = [127,0,0]
print(red.rgba)