def hasCycle(adjacencyLists):
    """
    Depth-first search.
    Return if any adjacent node is already in this depth-first tree.
    """
    nodes = adjacencyLists.keys()
    searchPhases = {}
    for node in nodes:
        searchPhases[node] = 0
    fromNodes = []
    parents = []
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
