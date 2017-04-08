from unittest import main, TestCase

from heap import *


class TestHeap(TestCase):
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

    def testPopMaxHeap1(self):
        maxHeap = [5]
        self.assertEquals(popMaxHeap(maxHeap), 5)
        self.assertEquals(maxHeap, [])

    def testPopMaxHeap3(self):
        maxHeap = [4, 3, 2]
        self.assertEquals(popMaxHeap(maxHeap), 4)
        self.assertEquals(maxHeap, [3, 2])

    def testPopMaxHeap5(self):
        maxHeap = [6, 2, 3, 0, 1]
        self.assertEquals(popMaxHeap(maxHeap), 6)
        self.assertEquals(maxHeap, [3, 2, 1, 0])

    def testIncreaseMaxHeap(self):
        maxHeap = [6, 2, 3, 0, 1]
        increaseMaxHeap(maxHeap, 2, 7)
        self.assertEquals(maxHeap, [7, 2, 6, 0, 1])

    def testIncreaseMaxHeap(self):
        maxHeap = [4]
        increaseMaxHeap(maxHeap, 0, 8)
        self.assertEquals(maxHeap, [8])

    def testInsertMaxHeap(self):
        maxHeap = [6, 2, 3, 0, 1]
        insertMaxHeap(maxHeap, 4)
        self.assertEquals(maxHeap, [6, 2, 4, 0, 1, 3])


if '__main__' == __name__:
    main()
