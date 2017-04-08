def countingSort(positiveIntegers):
    """
    Linear-time as described in the book.
    """
    if not positiveIntegers:
        return
    counts = getCountsList(positiveIntegers)
    for index in range(1, len(counts)):
        counts[index] += counts[index - 1]
    sortedLength = len(positiveIntegers)
    sortedIntegers = [0] * sortedLength
    for originalIndex in range(sortedLength - 1, -1, -1):
        integer = positiveIntegers[originalIndex]
        counts[integer] -= 1
        sortedIndex = counts[integer]
        sortedIntegers[sortedIndex] = integer
    positiveIntegers[:] = sortedIntegers[:]


def countingSortSimple(positiveIntegers):
    """
    Slower than linear time if there many gaps,
    because loops over all integers in gaps.
    With few gaps this is faster than linear time counting sort.
    """
    if not positiveIntegers:
        return
    counts = getCountsList(positiveIntegers)
    sortedIndex = len(positiveIntegers)
    for index in range(len(counts) - 1, -1, -1):
        while 1 <= sortedIndex and 0 < counts[index]:
            sortedIndex -= 1
            positiveIntegers[sortedIndex] = index
            counts[index] -= 1


def getCountsList(positiveIntegers):
    """
    Expects each positive integer is between 0 and a finite array size.
    For simplicity this example is limited to 32-bits.
    """
    largest = float('-inf')
    maximum = (1 << 32) - 1
    minimum = 0
    for integer in positiveIntegers:
        if not isinstance(integer, int) or integer < minimum or maximum < integer:
            raise TypeError('Expected integer between %r and %r. Got %r'
                % (minimum, maximum, integer))
        if largest < integer:
            largest = integer
    length = largest + 1
    counts = [0] * length
    for integer in positiveIntegers:
        counts[integer] += 1
    return counts


if '__main__' == __name__:
    from sortargs import printSortArgs
    printSortArgs(countingSort, type=int)
