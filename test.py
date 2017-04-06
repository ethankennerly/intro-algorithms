"""
Recursively unit test and doctest subdirectories.
"""


import doctest
import pkgutil
import unittest


testFilePaths = ['README.md']


def findModules(path = '.'):
    """
    http://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package
    """
    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(path):
        module = __import__(modname, fromlist='dummy')
        modules.append(module)
    return modules


class TestDocTests(unittest.TestCase):

    modules = findModules()

    def doctest(self, mod):
        """
        http://stackoverflow.com/questions/16982514/python-test-discovery-with-doctests-coverage-and-parallelism
        """
        self.assertTrue(doctest.testmod(mod))

    def testDoctests(self):
        for module in self.modules:
            self.doctest(module)


def runDiscoveredTests():
    """
    Similar to command line:  python -m unittest discover
    http://stackoverflow.com/questions/1732438/how-to-run-all-python-unit-tests-in-a-directory
    """
    suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner().run(suite)


if '__main__' == __name__:
    runDiscoveredTests()
    from doctest import testfile
    for path in testFilePaths:
        testfile(path)
