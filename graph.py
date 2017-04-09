def hasCycle(adjacencyLists):
    """
    Recursive depth-first search as described in the book adapted for detecting a cycle.
    Return if any adjacent node is already in this depth-first tree.
    """
    nodes = adjacencyLists.keys()
    searchPhases = {}
    for node in nodes:
        searchPhases[node] = 0
    for source in nodes:
        if hasDepthFirstCycle(adjacencyLists, source, searchPhases):
            return True
    return False


def hasDepthFirstCycle(adjacencyLists, fromNode, searchPhases):
    for toNode in adjacencyLists[fromNode]:
        if searchPhases[toNode] <= 0:
            searchPhases[toNode] = 1
            return hasDepthFirstCycle(adjacencyLists, toNode, searchPhases)
        elif 1 == searchPhases[toNode]:
            return True
    searchPhases[fromNode] = 2
    return False


def topologicalSort(adjacencyLists):
    """
    Return list of nodes sorted by predecessors first.
    Error if the graph has a cycle.
    """
    nodes = adjacencyLists.keys()
    searchPhases = {}
    for node in nodes:
        searchPhases[node] = 0
    order = []
    for source in nodes:
        postOrderSearch(adjacencyLists, source, searchPhases, order)
    return order


def postOrderSearch(adjacencyLists, fromNode, searchPhases, order):
    for toNode in adjacencyLists[fromNode]:
        if searchPhases[toNode] <= 0:
            searchPhases[toNode] = 1
            postOrderSearch(adjacencyLists, toNode, searchPhases, order)
        elif 1 == searchPhases[toNode]:
            raise Exception('Graph contains cycle at %r. Graph %r.' % (toNode, adjacencyLists))
    if fromNode not in order:
        order.insert(0, fromNode)
    searchPhases[fromNode] = 2
