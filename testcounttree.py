from unittest import TestCase, main


from counttree import *


class TestCountTree(TestCase):
    def testCountSmallerToTheRight(self):
        self.assertEqual(
            countSmallerToTheRight(
            [9, 0, 2, 9, 1]),
            [3, 0, 1, 1, 0])


if '__main__' == __name__:
    main()
