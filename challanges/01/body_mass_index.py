CATEGORIES = {
    'тежко недохранване': (float('-inf'), 15),
    'средно недохранване': (15, 16),
    'леко недохранване': (16, 18.5),
    'нормално тегло': (18.5, 25),
    'наднормено тегло': (25, 30),
    'затлъстяване I степен': (30, 35),
    'затлъстяване II степен': (35, 40),
    'затлъстяване III степен': (40, float('inf')),
}


def body_mass_index(weight, height):
    return round(weight / height ** 2, 1)


def shape_of(weight, height):
    bmi = body_mass_index(weight, height)

    for shape, bounderies in CATEGORIES.items():
        if (is_between(bmi, *bounderies)):
            return shape


def is_between(value, minimum, maximum):
    return minimum < value <= maximum
