from unittest import main, TestCase

from heapsort import *


class TestHeapsort(TestCase):
    def testMaxHeapifyOne(self):
        aList = [2]
        maxHeapify(aList, 0)
        self.assertEquals(aList, [2])

    def testMaxHeapifyThree(self):
        aList = [2, 4, 3]
        maxHeapify(aList, 0)
        self.assertEquals(aList, [4, 2, 3])

    def testBuildMaxHeap(self):
        aList = [2, 4, 3]
        buildMaxHeap(aList)
        self.assertEquals(aList, [4, 2, 3])

    def testHeapsort(self):
        aList = [2, 4, 3]
        heapsort(aList)
        self.assertEquals(aList, [2, 3, 4])


if '__main__' == __name__:
    main()
