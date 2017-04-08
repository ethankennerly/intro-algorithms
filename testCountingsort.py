from unittest import TestCase, main

from countingsort import *


class TestCountingSort(TestCase):
    def testCountingSortEmpty(self):
        integers = []
        countingSort(integers)
        self.assertEquals(integers, [])

    def testCountingSortDuplicate(self):
        integers = [0, 3, 2, 0]
        countingSort(integers)
        self.assertEquals(integers, [0, 0, 2, 3])

    def testCountingSortSimpleEmpty(self):
        integers = []
        countingSortSimple(integers)
        self.assertEquals(integers, [])

    def testCountingSortSimpleDuplicate(self):
        integers = [0, 3, 2, 0]
        countingSortSimple(integers)
        self.assertEquals(integers, [0, 0, 2, 3])

    def testCountingSortMixedTypeError(self):
        mixedTypes = [0, 3, '2', 'a']
        self.assertRaises(TypeError, countingSort, mixedTypes)

    def testCountingSortNegativeError(self):
        mixedTypes = [0, 2, -1]
        self.assertRaises(TypeError, countingSort, mixedTypes)


if '__main__' == __name__:
    main()
