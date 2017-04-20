from unittest import TestCase, main

from binarytree import *


class TestBinaryTree(TestCase):
    def testInOrderTraverse(self):
        root = createTree([4,
                            [[2,
                               [1, 3]],
                              6]])
        self.assertEqual(inOrderTraverse(root),
            [1, 2, 3, 4, 6]);


if '__main__' == __name__:
    main()
