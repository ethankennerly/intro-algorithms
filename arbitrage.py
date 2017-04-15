def isArbitrage(exchangeRateMatrix, roundingError = 0.00001):
    """
    Abitrage: Profiting from discrepancies in exchange rate.

    isArbitrage function returns if there is a path of exchanges that yields a profit.
    If the exchange rate graph has a sink currency, that can be exchanged to with varying efficiency,
    this is also detected.
    By sink currency, I mean a currency that cannot be exchanged from.

    exchangeRateMatrix:  Weighted directed adjacency matrix.
    M[i][j] represents exchange rate from currency i to j.

    Answering question 24-3 on page 679.

    Strategy:
    From each node in a graph,
    travel along non-zero edges until complete or cycle.
    Along each step multiply value.
    At each cycle, if the value is greater than starting value, there is an opportunity for arbitrage.
    """
    nodeCount = len(exchangeRateMatrix)
    nodes = range(nodeCount)
    tolerance = 1.0 + roundingError
    for startNode in nodes:
        startValue = 1.0
        values = [0.0] * nodeCount
        currentValue = startValue
        visits = [0] * nodeCount
        values[startNode] = currentValue
        nodeStack = [startNode]
        while nodeStack:
            previous = nodeStack.pop()
            if 2 == visits[previous]:
                continue
            visits[previous] = 2
            for next in nodes:
                rate = exchangeRateMatrix[previous][next]
                if not rate:
                    continue
                currentValue = rate * values[previous]
                if visits[next] \
                and not isEqual(currentValue, values[next], tolerance):
                    return True
                if not visits[next]:
                    visits[next] = 1
                    values[next] = currentValue
                    nodeStack.append(next)
    return False


def isEqual(currentValue, startValue, tolerance = 1.0001):
    return (currentValue == startValue) \
        or ((currentValue / tolerance) \
            < startValue < (currentValue * tolerance))
