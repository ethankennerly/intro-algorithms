from sys import argv


def printSortArgs(sort, aList = None):
    if aList is None:
        aList = argv[1:]
    print('Sorting from:\n    %r' % aList)
    sort(aList)
    print('to:\n    %r' % aList)
