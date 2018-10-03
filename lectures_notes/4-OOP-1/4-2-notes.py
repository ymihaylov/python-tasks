# 1. Абстракция
# 2. Енкапсулация
# 3. Модулярност

# Всичко е обект
# Обектите са отворени
# Класовете са отворени

type(42)  # Check the type of object

# Класове се създават с ключовата дума class, след което всяка функция е метод
# и всяка променлива е клас променлива


class Vector:
    # Constructor, doesn't return value (initializator)
    # First argument is always named self
    # Attributes doesn't need declaration (Classes are open)
    # But __init__ is not very first function that python invokes
    def __init__(self, x, y):
        self.x = x
        self.y = y


spam = Vector(1.0, 1.5)
print(spam.x)
