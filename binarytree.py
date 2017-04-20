from collections import deque


class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = [None, None]


def createTree(treeList):
    if not treeList:
        return None
    if not isinstance(treeList, list):
        key = treeList
        child = Node(key)
        return child
    length = len(treeList)
    if length != 2:
        raise TypeError('Expected 2 or fewer nodes. Got %r items: %r' % (length, treeList))
    key, children = treeList
    child = Node(key)
    child.children[0] = createTree(children[0])
    child.children[1] = createTree(children[1])
    return child


def inOrderTraverse(node):
    keys = []
    if node is None:
        return keys
    if node.children[0]:
        keys.extend(inOrderTraverse(node.children[0]))
    keys.append(node.key)
    if node.children[1]:
        keys.extend(inOrderTraverse(node.children[1]))
    return keys


def preOrderTraverse(node):
    keys = []
    if node is None:
        return keys
    if node.children[0]:
        keys.extend(preOrderTraverse(node.children[0]))
    if node.children[1]:
        keys.extend(preOrderTraverse(node.children[1]))
    keys.append(node.key)
    return keys


def postOrderTraverse(node):
    keys = []
    if node is None:
        return keys
    keys.append(node.key)
    if node.children[0]:
        keys.extend(postOrderTraverse(node.children[0]))
    if node.children[1]:
        keys.extend(postOrderTraverse(node.children[1]))
    return keys


def levelOrderTraverse(root):
    keys = []
    if root is None:
        return keys
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        keys.append(node.key)
        for child in node.children:
            if child:
                queue.append(child)
    return keys
