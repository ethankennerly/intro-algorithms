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
