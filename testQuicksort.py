from unittest import main, TestCase

from quicksort import *


class TestQuicksort(TestCase):
    def testQuicksorts(self):
        aLists = [[], [5], [6, 7], [2, 4, 3]]
        for aList in aLists:
            quicksort(aList)
            self.assertEquals(aList, sorted(aList[:]))


if '__main__' == __name__:
    main()
