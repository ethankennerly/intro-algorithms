from unittest import TestCase, main

from arbitrage import *


class TestArbitrage(TestCase):

    def testIsArbitrageEmpty(self):
        rates = ()
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageOne(self):
        rates = ((1.0,),)
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageSelf(self):
        rates = ((2.0,),)
        self.assertEqual(isArbitrage(rates), True)

    def testIsArbitrageTwo(self):
        rates = ((1.0, 2.0),
                 (0.5, 1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageDirected(self):
        rates = ((1.0, 1.0),
                 (2.0, 1.0))
        self.assertEqual(isArbitrage(rates), True)

    def testIsArbitrageThree(self):
        rates = ((1.0,  0.5,  2.5),
                 (2.0,  1.0,  5.0),
                 (0.4,  0.2,  1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageBypassThird(self):
        rates = ((1.0,  0.5,  1.0),
                 (2.0,  1.0,  4.0),
                 (1.0,  0.25, 1.0))
        self.assertEqual(isArbitrage(rates), True)

    def testIsArbitrageBypassSecond(self):
        rates = ((1.0,  1.0,  0.5),
                 (1.0,  1.0,  1.0),
                 (2.0,  1.0,  1.0))
        self.assertEqual(isArbitrage(rates), True)

    def testIsArbitrageBridge(self):
        rates = ((1.0,  0.5,  0.0),
                 (2.0,  1.0,  4.0),
                 (0.0,  0.25, 1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageRounded(self):
        rates = ((1.0,  0.5,  2.50000001),
                 (2.0,  1.0,  4.99999999),
                 (0.4,  0.2,  1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageSmall(self):
        rates = ((1.0,  0.5,  2.501),
                 (2.0,  1.0,  5.0),
                 (0.4,  0.2,  1.0))
        self.assertEqual(isArbitrage(rates), True)

    def testIsArbitrageSinkEqual(self):
        rates = ((1.0,  0.5,  4.0),
                 (2.0,  1.0,  8.0),
                 (0.0,  0.0,  1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageSinkDiscrepant(self):
        rates = ((1.0,  0.5,  1.0),
                 (2.0,  1.0,  4.0),
                 (0.0,  0.0,  1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageSinkClusterDiscrepant(self):
        rates = ((1.0,  0.5,  1.0,  0.75),
                 (2.0,  1.0,  4.0,  0.2),
                 (0.0,  0.0,  1.0,  2.5),
                 (0.0,  0.0,  0.4,  1.0))
        self.assertEqual(isArbitrage(rates), False)


if '__main__' == __name__:
    main()
