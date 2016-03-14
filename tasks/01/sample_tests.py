import unittest

import working_with_pictures


class TestImages(unittest.TestCase):
    image = [
        [(0, 0, 255), (0, 255, 0), (0, 0, 255)],
        [(255, 0, 0), (0, 0, 255), (0, 255, 0)],
        [(0, 255, 0), (0, 255, 0), (255, 0, 0)]]

    def test_rotate_left(self):
        rotated = working_with_pictures.rotate_left(self.image)
        expected = [[(0, 0, 255), (0, 255, 0), (255, 0, 0)],
                    [(0, 255, 0), (0, 0, 255), (0, 255, 0)],
                    [(0, 0, 255), (255, 0, 0), (0, 255, 0)]]

        for i in range(len(expected)):
            for j in range(len(expected[0])):
                self.assertEqual(expected[i][j], rotated[i][j])

    def test_lighten(self):
        lighten = working_with_pictures.lighten(self.image, 0.5)
        expected = [[(127, 127, 255), (127, 255, 127), (127, 127, 255)],
                    [(255, 127, 127), (127, 127, 255), (127, 255, 127)],
                    [(127, 255, 127), (127, 255, 127), (255, 127, 127)]]

        for i in range(len(expected)):
            for j in range(len(expected[0])):
                self.assertEqual(expected[i][j], lighten[i][j])

    def test_invert(self):
        inverted = working_with_pictures.invert(self.image)
        expected = [[(255, 255, 0), (255, 0, 255), (255, 255, 0)],
                    [(0, 255, 255), (255, 255, 0), (255, 0, 255)],
                    [(255, 0, 255), (255, 0, 255), (0, 255, 255)]]

        for i in range(len(expected)):
            for j in range(len(expected[0])):
                self.assertEqual(expected[i][j], inverted[i][j])

    def test_create_histogram(self):
        self.assertEqual(
            working_with_pictures.create_histogram(self.image),
            {'blue': {0: 6, 255: 3},
             'green': {0: 5, 255: 4},
             'red': {0: 7, 255: 2}})


if __name__ == '__main__':
    unittest.main()
