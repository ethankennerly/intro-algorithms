from sortargs import printSortArgs


def quicksort(aList):
    begin = 0
    end = len(aList) - 1
    if end <= begin:
        return
    beginsAndEnds = [(begin, end)]
    while beginsAndEnds:
        begin, end = beginsAndEnds.pop()
        if begin < end:
            middle = begin
            for index in range(begin + 1, end):
                if aList[middle] <= aList[end]:
                    aList[end], aList[index] = aList[index], aList[end]
                    middle += 1
            if begin < middle:
                beginsAndEnds.append((begin, middle - 1))
            if middle < end:
                beginsAndEnds.append((middle + 1, end))


if '__main__' == __name__:
    printSortArgs(quicksort)
