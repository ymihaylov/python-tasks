image = [
    [(0, 0, 255), (0, 255, 0), (0, 0, 255)],
    [(255, 0, 0), (0, 0, 255), (0, 255, 0)],
    [(0, 255, 0), (0, 255, 0), (255, 0, 0)]
]


def transponse_image(image):
    return ([list(x) for x in zip(*image)])


def rotate_left(image):
    image = transponse_image(image)

    return image[::-1]


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
    return [[(127, 127, 255), (127, 255, 127), (127, 127, 255)],
            [(255, 127, 127), (127, 127, 255), (127, 255, 127)],
            [(127, 255, 127), (127, 255, 127), (255, 127, 127)]]


# lighten(image)

# [[(127, 127, 255), (127, 255, 127), (127, 127, 255)],
# [(255, 127, 127), (127, 127, 255), (127, 255, 127)],
# [(127, 255, 127), (127, 255, 127), (255, 127, 127)]]
