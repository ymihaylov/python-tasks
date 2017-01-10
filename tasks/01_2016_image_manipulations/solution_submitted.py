image = [
    [(0, 0, 255), (0, 255, 0), (0, 0, 255)],
    [(255, 0, 0), (0, 0, 255), (0, 255, 0)],
    [(0, 255, 0), (0, 255, 0), (255, 0, 0)]
]


def create_histogram(image):
    rgb_dict = {
        'red': [],
        'green': [],
        'blue': [],
    }

    for row in image:
        ([
            (
                rgb_dict['red'].append(x),
                rgb_dict['green'].append(y),
                rgb_dict['blue'].append(z)
            ) for x, y, z in row
        ])

    for color_name in rgb_dict:
        rgb_dict[color_name] = dict(
            (i, rgb_dict[color_name].count(i)) for i in rgb_dict[color_name]
        )

    return(rgb_dict)


def transponse_image(image):
    return ([list(x) for x in zip(*image)])


def lighten_value(value, factor):
    return int(value + factor * (255 - value))


def darken_value(value, factor):
    return int(value - factor * (value - 0))


def grayscale(fun):
    def decorator(*args, **kwargs):
        image = fun(*args, **kwargs)

        return grayscale_image(image)

    return decorator


def grayscale_image(image):
    return [[grayscale_pixel(pixel) for pixel in row] for row in image]


def grayscale_pixel(pixel):
    grayscale_value = int(
        0.2126 * pixel[0] +
        0.7152 * pixel[1] +
        0.0722 * pixel[2]
    )

    return (grayscale_value, grayscale_value, grayscale_value)


@grayscale
def rotate_left(image):
    image = transponse_image(image)

    return image[::-1]

print(rotate_left(image))


def rotate_right(image):
    image = transponse_image(image)

    image_rotated = []

    for row in image:
        image_rotated.append(row[::-1])

    return image_rotated


def invert(image):
    inverted_image = []

    for row in image:
        inverted_row = []

        for pixel in row:
            inverted_row.append(
                (tuple(x - y for x, y in zip((255, 255, 255), pixel)))
            )

        inverted_image.append(inverted_row)

    return inverted_image


def lighten(image, factor):
    lighten_image = []
    for row in image:
        lighten_image.append([
            (
                lighten_value(x, factor),
                lighten_value(y, factor),
                lighten_value(z, factor)
            ) for x, y, z in row
        ])

    return lighten_image


def darken(image, factor):
    darken_image = []

    for row in image:
        darken_image.append([
            (
                darken_value(x, factor),
                darken_value(y, factor),
                darken_value(z, factor)
            ) for x, y, z in row
        ])

    return darken_image
