def transponse_image(image):
    return [list(x) for x in zip(*image)]


def rotate_left(image):
    return transponse_image(image)[::-1]


def rotate_right(image):
    image = transponse_image(image)
    result = [x[::-1] for x in image]

    return result


def invert(image):
    inverted_image = []
    for row in image:
        inverted_pixels = [
            tuple(255 - pixel_value for pixel_value in pixel)
            for pixel in row
        ]

        inverted_image.append(inverted_pixels)

    return inverted_image


def lighten(image, factor):
    lighten_image = []

    for row in image:
        lighten_image.append([lighten_pixel(pixel, factor) for pixel in row])

    return lighten_image


def lighten_pixel(pixel, factor):
    return tuple(
        int(pixel_value + factor * (255 - pixel_value))
        for pixel_value in pixel
    )


def darken(image, factor):
    darken_image = []

    for row in image:
        darken_image.append([darken_pixel(pixel, factor) for pixel in row])

    return darken_image


def darken_pixel(pixel, factor):
    return tuple(
        int(pixel_value - factor * (pixel_value - 0))
        for pixel_value in pixel
    )


def create_histogram(image):
    rgb_dict = {
        'red': [],
        'green': [],
        'blue': []
    }

    for row in image:
        for pixel in row:
            rgb_dict['red'].append(pixel[0])
            rgb_dict['green'].append(pixel[1])
            rgb_dict['blue'].append(pixel[2])

    for color, values in rgb_dict.items():
        rgb_dict[color] = {value: values.count(value) for value in values}

    return rgb_dict
