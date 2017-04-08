def countingSort(positiveIntegers):
    """Expects each positive integer is between 0 and a finite array size.
    For simplicity this example is limited to 32-bits.
    """
    if not positiveIntegers:
        return
    smallest = float('inf')
    largest = float('-inf')
    maximum = (1 << 32) - 1
    minimum = 0
    for integer in positiveIntegers:
        if not isinstance(integer, int) or integer < minimum or maximum < integer:
            raise TypeError('Expected integer between %r and %r. Got %r'
                % (minimum, maximum, integer))
        if integer < smallest:
            smallest = integer
        if largest < integer:
            largest = integer
    length = largest + 1
    counts = [0] * length
    for integer in positiveIntegers:
        counts[integer] += 1
    for index in range(1, length):
        counts[index] += counts[index - 1]
    sortedIndex = len(positiveIntegers)
    for index in range(largest, -1, -1):
        if 1 <= index:
            previousCount = counts[index - 1]
        else:
            previousCount = 0
        while 1 <= sortedIndex and previousCount < counts[index]:
            sortedIndex -= 1
            positiveIntegers[sortedIndex] = index
            counts[index] -= 1


if '__main__' == __name__:
    from sortargs import printSortArgs
    printSortArgs(countingSort, type=int)
