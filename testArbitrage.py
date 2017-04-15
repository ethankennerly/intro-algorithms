from unittest import TestCase, main

from arbitrage import *


class TestArbitrage(TestCase):

    def testIsArbitrageEmpty(self):
        rates = ()
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageOne(self):
        rates = ((1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageSelf(self):
        rates = ((2.0))
        self.assertEqual(isArbitrage(rates), True)

    def testIsArbitrageTwo(self):
        rates = ((1.0, 2.0),
                 (0.5, 1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageOneWay(self):
        rates = ((1.0, 1.0),
                 (2.0, 1.0))
        self.assertEqual(isArbitrage(rates), True)

    def testIsArbitrageThree(self):
        rates = ((1.0,  0.5,  2.5),
                 (2.0,  1.0,  5.0),
                 (0.4,  0.2,  1.0))
        self.assertEqual(isArbitrage(rates), False)

    def testIsArbitrageThreeBypass(self):
        rates = ((1.0,  0.5,  1.0),
                 (2.0,  1.0,  4.0),
                 (1.0,  0.25, 1.0))
        self.assertEqual(isArbitrage(rates), True)


if '__main__' == __name__:
    main()
