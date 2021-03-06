from unittest import TestCase, main

from graph import *


class TestGraph(TestCase):
    def testHasCycleTree(self):
        adjacencyLists = {0: [1, 2], 1: [], 2: []}
        self.assertEquals(hasCycle(adjacencyLists), False)

    def testHasCycleLoop(self):
        adjacencyLists = {0: [1, 2], 1: [], 2: [0]}
        self.assertEquals(hasCycle(adjacencyLists), True)

    def testHasCycleMergeLeaf(self):
        adjacencyLists = {0: [1, 2], 1: [], 2: [1]}
        self.assertEquals(hasCycle(adjacencyLists), False)

    def testHasCycleMerge(self):
        adjacencyLists = {0: [1, 2], 1: [3], 2: [1], 3: []}
        self.assertEquals(hasCycle(adjacencyLists), False)

    def testTopologicalSort(self):
        adjacencyLists = {0: [1, 2], 1: [3], 2: [1], 3: []}
        self.assertEquals(topologicalSort(adjacencyLists), [0, 2, 1, 3])

    def testTopologicalSortLoopError(self):
        adjacencyLists = {0: [1, 2], 1: [], 2: [0]}
        self.assertRaises(Exception, topologicalSort, adjacencyLists)


if '__main__' == __name__:
    main()
