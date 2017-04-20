from unittest import TestCase, main

from binarytree import *


root = createTree([4,
                    [[2,
                       [1, 3]],
                      6]])


class TestBinaryTree(TestCase):
    def testInOrderTraverse(self):
        self.assertEqual(inOrderTraverse(root),
            [1, 2, 3, 4, 6]);

    def testPreOrderTraverse(self):
        self.assertEqual(preOrderTraverse(root),
            [1, 3, 2, 6, 4]);

    def testPostOrderTraverse(self):
        self.assertEqual(postOrderTraverse(root),
            [4, 2, 1, 3, 6]);

    def testLevelOrderTraverse(self):
        self.assertEqual(levelOrderTraverse(root),
            [4, 2, 6, 1, 3]);


if '__main__' == __name__:
    main()
