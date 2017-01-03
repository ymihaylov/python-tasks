WESTERN_SIGNS = [
    ('aquarius', 21, 1),
    ('pisces', 19, 2),
    ('aries', 21, 3),
    ('taurus', 21, 4),
    ('gemini', 21, 5),
    ('cancer', 21, 6),
    ('leo', 23, 7),
    ('virgo', 23, 8),
    ('libra', 23, 9),
    ('scorpio', 23, 10),
    ('sagittarius', 22, 11),
    ('capricorn', 22, 12),
]

CHINESE_SIGNS = [
    'monkey',
    'rooster',
    'dog',
    'pig',
    'rat',
    'ox',
    'tiger',
    'rabbit',
    'dragon',
    'snake',
    'horse',
    'sheep',
]


def interpret_western_sign(day, month):
    sign = WESTERN_SIGNS[month - 1]
    if (day >= sign[1]):
        return sign[0]

    previous_sign = WESTERN_SIGNS[month - 2]
    return previous_sign[0]


def interpret_chinese_sign(year):
    return CHINESE_SIGNS[year % len(CHINESE_SIGNS)]


def interpret_both_signs(day, month, year):
    return (interpret_western_sign(day, month), interpret_chinese_sign(year))
