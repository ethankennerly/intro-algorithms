from sortargs import printSortArgs


def maxHeapify(aList, index, heapSize = -1):
    if -1 == heapSize:
        heapSize = len(aList)
    indexOfLargest = -1
    while index != indexOfLargest and index < heapSize:
        largestValue = aList[index]
        address = index + 1
        leftChild = address * 2 - 1
        rightChild = leftChild + 1
        if leftChild < heapSize and largestValue < aList[leftChild]:
            indexOfLargest = leftChild
            largestValue = aList[leftChild]
        else:
            indexOfLargest = index
        if rightChild < heapSize and largestValue < aList[rightChild]:
            indexOfLargest = rightChild
        if index != indexOfLargest:
            aList[index], aList[indexOfLargest] = aList[indexOfLargest], aList[index]
            index = indexOfLargest


def buildMaxHeap(aList):
    indexes = range(len(aList) - 1, -1, -1)
    for index in indexes:
        maxHeapify(aList, index)


def heapsort(aList):
    buildMaxHeap(aList)
    indexes = range(len(aList) - 1, 0, -1)
    for index in indexes:
        aList[index], aList[0] = aList[0], aList[index]
        maxHeapify(aList, 0, index)


def popMaxHeap(maxHeap):
    largest = maxHeap[0]
    last = maxHeap.pop()
    if 2 <= len(maxHeap):
        maxHeap[0] = last
        maxHeapify(maxHeap, 0)
    return largest


def increaseMaxHeap(maxHeap, index, nextValue):
    if nextValue < maxHeap[index]:
        raise Error('Expected %r less than %r' % (
            nextValue, maxHeap[index]))
    maxHeap[index] = nextValue
    parent = (index - 1) >> 1
    while maxHeap[parent] < maxHeap[index]:
        maxHeap[parent], maxHeap[index] = maxHeap[index], maxHeap[parent]
        index = parent
        parentIndex = (index - 1) >> 1


if '__main__' == __name__:
    printSortArgs(heapsort)
