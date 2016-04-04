# del - delete attributes from 
# __getitem__

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, i):
        return (self.x, self.y, self.z)[i]

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            pass

    def __str__(self):
        return str((self.x, self.y, self.z))

    def __len__(self):
        return 3

    def __add__(self, other):
         return Vector(*map(sum, zip(self, other)))

# there has delattr(obj, 'name')
# __getattr__ calls only when object doesnt have attribute
# __getattribute__ - for all 

v1 = Vector(1, 2, 3)
print(v1.__dict__)
print(v1.__class__ is Vector)

# When calls baba.attr than:
# Search  baba.__dict__['attr']
# Search  baba.__class__.attr
	# - if its not function then return direct
	# - if its function then bound method
# Search baba.__getattr__('attr')

# ---

# Everything extends Object

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return self.first_name + " " + self.last_name

class Star(Person):
    def greet_audience(self):
        print("Hello Sofia, I am {0}!".format(self.name()))

david = Star("David", "Gahan")
david.greet_audience()

# ----
class Spam:
    def spam(self): return "spam"

class Eggs:
    def eggs(self): return "eggs"

class CheeseShop(Spam, Eggs):
    def food(self):
        return self.spam() + " and " + self.eggs()

# ---
# MixinClasses 
# Mixin - as abstract
# name mangling

class Base:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def report_base(self):
        print("Base:", self.__name, self._age)

class Derived(Base):
    def __init__(self, name, age, derived_name):
        Base.__init__(self, name, age)
        self.__name = derived_name
        self._age = 33

    def report_derived(self):
        print("Derived:", self.__name, self._age)

derived = Derived("John", 0, "Doe")
print(derived.report_base()) # Base: John 33
print(derived.report_derived()) # Derived: Doe 33
# print(derived._Base__name, derived._Derived__name, sep=', ') # John, Doe

# isinstance and issubclass