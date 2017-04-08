from unittest import TestCase, main

from countingsort import countingSort


class TestCountingSort(TestCase):
    def testCountingSort(self):
        integers = [0, 3, 2, 0]
        countingSort(integers)
        self.assertEquals(integers, [0, 0, 2, 3])


if '__main__' == __name__:
    main()
