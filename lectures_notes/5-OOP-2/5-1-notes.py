# del pesho.age - изтриваме атрибути от обект с del


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
            pass  # we can raise exception here

    def __str__(self):
        return str((self.x, self.y, self.z))

    def __len__(self):
        return 3

    def __add__(self, other):
        return Vector(*map(sum, zip(self, other)))


v = Vector(3, 4, 5)
v[0] = 5
# print(v.x)

# __getitem__ - когато достъпваме v[0], v[1] etc.
# __str__ - to string
# __len__ - when len() is invoked

###

# Dynamic methods for classes
# getattr(obj, 'name', default) е като obj.name
# setattr(obj, 'name', value) е като obj.name = value
# delattr(obj, 'name') е като del obj.name

# Предефиниране достъпването на атрибути на нашите обекти
# __getattr__(self, name) - извиква се ако атрибута няма name (само тогава)
# __getattribute__ - предефиниране на достъпване винаги (и когато съществува)
# __setattr__(self, name, value) -
# __delattr__(self, name)


class SpamOld:
    def __init__(self):
        self.eggs = 12

    def __getattr__(self, name):
        return name.upper()

    def __setattr__(self, name, value):
        print("Setting {0} to {1}".format(name, value))
        return object.__setattr__(self, name.upper(), value + 10)

    def answer(self):
        return 42

# spam = SpamOld()
# spam.foo = 42
# print(spam.foo)
# print(spam)
# print(spam.answer())


class Spam2:
    pass

spam = Spam2()
spam.foo = 1
spam.bar = 2
# print(spam.__dict__)  # {'foo': 1, 'bar': 2}
# print(spam.__class__)  # <class '__main__.Spam'>
# print(spam.__class__ is Spam)  # True

# И функциите и обектите са атрибути на класа

###
# Objects and pythons
# When is called baba.attr:
# 1) Returns baba.__dict__['attr'] if it exists
# 2) Search in baba.__class__.__attr__
# 3) baba.__getattr__('attr')

###
# Inheritance
# Every objects extends object


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Star(Person):
    def greet_audience(self):
        print("Hello Sofia, I am {0}!".format(self.name()))


class Japanese(Person):
    def name(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Doctor(Person):
    def name(self):
        return '{}, M.D.'.format(Person.name(self))

# david = Star("David", "Gahan")
# david.greet_audience()
# print(Person("Edward", "Murdsone").name())  # Edward Murdstone
# print(Japanese("Yukihiro", "Matsumoto").name())  # Matsumoto Yukihiro
# print(Doctor("Gregory", "House").name())

# Multiple Inheritance


class Spam:
    def spam(self):
        return 'spam'

    def eggs(self):
        return 'spam'


class Eggs:
    def eggs(self):
        return 'eggs'


class CheeseShop(Spam, Eggs):
    def food(self):
        return self.spam() + ' and ' + self.eggs()


###
# Mixins - добра причина (една от малкото) за използване на множествено насл.
# Не се използват сами по себе си. Написани са за да се наследяват

###
# Name mangling


class Test:
    def __init__(self):
        self.__var = 42

t = Test

# print(dir(Test()))  # ['_Test__var', '__class__', ...]

###
# Private and protected


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
# print(derived.report_base())    # Base: John 33
# print(derived.report_derived())     # Derived: Doe 33
# print(derived._Base__name)    # John, Doe
# print(derived._Derived__name)

###
# isinstance
# issubclass
