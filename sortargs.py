from sys import argv


def printSortArgs(sort, aList = None, type=None):
    if aList is None:
        aList = argv[1:]
    if type:
        aList = [type(item) for item in aList]
    print('Sorting from:\n    %r' % aList)
    sort(aList)
    print('to:\n    %r' % aList)
