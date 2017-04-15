def isArbitrage(exchangeRateMatrix, roundingError = 0.00001, isVerbose = False):
    """
    Abitrage: Profiting from discrepancies in exchange rate.

    isArbitrage function returns if there is a path of exchanges that yields a profit.
    If the exchange rate graph has a sink currency, that can be exchanged to with varying efficiency,
    this is not detected.
    By sink currency, I mean a currency that cannot be exchanged from.

    exchangeRateMatrix:  Weighted directed adjacency matrix.
    M[i][j] represents exchange rate from currency i to j.

    Answering question 24-3 on page 679.

    isVerbose:  Returns if discrepant values and all values.

    Strategy:
    Dynamically program reachable nodes and values.
    From each node in a graph,
    travel along non-zero edges until complete or cycle.
    Along each step multiply value.
    At each cycle, if the value is greater than starting value, there is an opportunity for arbitrage.
    There is no opportunity for arbitrage if the destination node cannot reach the source node.

    If the graph is sparsely connected, then an adjacency list would scale quicker than an adjacency matrix.
    O(v^2) > O(ve) if e is small.
    """
    nodeCount = len(exchangeRateMatrix)
    nodes = range(nodeCount)
    tolerance = 1.0 + roundingError
    reachableMatrix = [[False for _ in nodes] for _ in nodes]
    values = [[0.0 for _ in nodes] for _ in nodes]
    discrepantDestinations = []
    for source in nodes:
        values[source][source] = 1.0
        nodeStack = [source]
        while nodeStack:
            previous = nodeStack.pop()
            for next in nodes:
                rate = exchangeRateMatrix[previous][next]
                if not rate:
                    continue
                nextValue = rate * values[source][previous]
                isVisited = reachableMatrix[source][next]
                sourceValue = values[source][next]
                if isVisited \
                and not isEqual(nextValue, sourceValue, tolerance):
                    discrepantDestinations.append((source, previous, next,
                        nextValue, sourceValue))
                if not isVisited:
                    values[source][next] = nextValue
                    reachableMatrix[source][next] = True
                    nodeStack.append(next)
                isVisited = reachableMatrix[source][previous] = True
    for source, previous, destination, nextValue, sourceValue in discrepantDestinations:
        if reachableMatrix[destination][source]:
            if isVerbose:
                return discrepantDestinations, values, nextValue, sourceValue
            else:
                return True
    return False


def isEqual(nextValue, sourceValue, tolerance = 1.0001):
    return (nextValue == sourceValue) \
        or ((nextValue / tolerance) \
            < sourceValue < (nextValue * tolerance))
