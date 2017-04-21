def countSmallerToTheRight(values):
    """
    Codefights.com interview practice question from Google by the same name.

    My first submission was to bisect a sorted list,
    which I new had O(n) insertion time complexity.
    After a search on the internet,
    I see how I could index in O(log n),
    I read nneoneo's algorithm outline to count in the binary tree.
    http://stackoverflow.com/questions/25251340/in-a-bst-find-count-of-nodes-smaller-greater-than-a-given-node-in-olog-n
    """
    if not values:
        return []
    length = len(values)
    counts = [0] * length
    indexes = range(length - 2, -1, -1)
    root = CountTreeNode(values[0])
    for index in indexes:
        value = values[index]
        child = insert(root, value)
        counts[index] = countSmaller(child)
    return counts


class CountTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.numDescendents = 0
        self.children = [None, None]


def insert(root, value):
    parent = root
    while True:
        parent.numDescendents += 1
        childIndex = 1 if parent.value < value else 0
        children = parent.children
        child = children[childIndex]
        if child:
            parent = child
        else:
            child = CountTreeNode(value)
            children[childIndex] = child
            child.parent = parent
            return child


def countSmaller(newChild):
    count = 0
    child = newChild
    smaller = child.children[0]
    if smaller:
        count += smaller.numDescendents
    parent = child.parent
    while parent:
        isGreater = parent.children[1] == child
        if isGreater:
            count += 1
            smaller = parent.children[0]
            if smaller:
                count += smaller.numDescendents
        child = parent
        parent = child.parent
    return count
