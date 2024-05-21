# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import unittest
from differentiate import *

import unittest


class variableX(unittest.TestCase):

    def test_x(self):
        x = variableAST("x")
        self.assertEqual("x", x.value0)

        xPrime = x._diff()
        self.assertTrue(isinstance(xPrime, numberAST))
        self.assertEqual(xPrime.value0, 1)


class plainTrigonometricDifferentiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_sinX(self):
        sinX = sinAST(self.variableX)
        sinX_prime = sinX._diff()

        self.assertTrue(isinstance(sinX_prime, cosAST))
        self.assertTrue(isinstance(sinX_prime.value0, variableAST))

    def test_cosX(self):
        cosX = cosAST(self.variableX)
        cosX_prime = cosX._diff()

        self.assertTrue(isinstance(cosX_prime, negativeAST))
        self.assertTrue(isinstance(cosX_prime.value0, sinAST))
        self.assertTrue(isinstance(cosX_prime.value0.value0, variableAST))
        self.assertEqual(cosX_prime.value0.value0.value0, self.variableConstant)

    def test_tanX(self):
        tanX = tanAST(self.variableX)
        tanX_prime = tanX._diff()

        self.assertTrue(isinstance(tanX_prime, sec2AST))
        self.assertTrue(isinstance(tanX_prime.value0, variableAST))
        self.assertEqual(tanX_prime.value0.value0, self.variableConstant)

    def test_secX(self):
        secX = secAST(self.variableX)
        secX_prime = secX._diff()

        self.assertTrue(isinstance(secX_prime, multAST))

        self.assertTrue(isinstance(secX_prime.value0, secAST))
        self.assertTrue(isinstance(secX_prime.value0.value0, variableAST))
        self.assertEqual(secX_prime.value0.value0.value0, self.variableConstant)

        self.assertTrue(isinstance(secX_prime.value1, tanAST))
        self.assertTrue(isinstance(secX_prime.value1.value0, variableAST))
        self.assertEqual(secX_prime.value1.value0.value0, self.variableConstant)

    def test_cscX(self):
        cscX = cscAST(self.variableX)
        cscX_prime = cscX._diff()

        self.assertTrue(isinstance(cscX_prime, negativeAST))
        self.assertTrue(isinstance(cscX_prime.value0, multAST))

        self.assertTrue(isinstance(cscX_prime.value0.value0, cscAST))
        self.assertTrue(isinstance(cscX_prime.value0.value0.value0, variableAST))
        self.assertEqual(cscX_prime.value0.value0.value0.value0, self.variableConstant)

        self.assertTrue(isinstance(cscX_prime.value0.value1, cotAST))
        self.assertTrue(isinstance(cscX_prime.value0.value1.value0, variableAST))
        self.assertEqual(cscX_prime.value0.value1.value0.value0, self.variableConstant)

    def test_cotX(self):
        cotX = cotAST(self.variableX)
        cotX_prime = cotX._diff()

        self.assertTrue(isinstance(cotX_prime, negativeAST))
        self.assertTrue(isinstance(cotX_prime.value0, csc2AST))
        self.assertTrue(isinstance(cotX_prime.value0.value0, variableAST))
        self.assertEqual(cotX_prime.value0.value0.value0, self.variableConstant)

    def test_arcsinX(self):
        arcsineX = arcsineAST(self.variableX)
        arcsineX_prime = arcsineX._diff()

        self.assertTrue(isinstance(arcsineX_prime, divAST))

        self.assertTrue(isinstance(arcsineX_prime.value0, numberAST))
        self.assertEqual(arcsineX_prime.value0.value0, 1)

        self.assertTrue(isinstance(arcsineX_prime.value1, powAST))
        self.assertTrue(isinstance(arcsineX_prime.value1.value0, subAST))
        self.assertTrue(isinstance(arcsineX_prime.value1.value0.value0, numberAST))
        self.assertEqual(arcsineX_prime.value1.value0.value0.value0, 1)

        self.assertTrue(isinstance(arcsineX_prime.value1.value0.value1, powAST))
        self.assertTrue(
            isinstance(arcsineX_prime.value1.value0.value1.value0, variableAST)
        )
        self.assertEqual(arcsineX_prime.value1.value0.value1.value0.value0, "x")

        self.assertTrue(
            isinstance(arcsineX_prime.value1.value0.value1.value1, numberAST)
        )
        self.assertEqual(arcsineX_prime.value1.value0.value1.value1.value0, 2)

    def test_arrcosineX(self):
        arccosineX = arccosineAST(self.variableX)
        arccosineX_prime = arccosineX._diff()

        self.assertTrue(isinstance(arccosineX_prime, negativeAST))

        self.assertTrue(isinstance(arccosineX_prime.value0, divAST))

        self.assertTrue(isinstance(arccosineX_prime.value0.value0, numberAST))
        self.assertEqual(arccosineX_prime.value0.value0.value0, 1)

        self.assertTrue(isinstance(arccosineX_prime.value0.value1, powAST))
        self.assertTrue(isinstance(arccosineX_prime.value0.value1.value0, subAST))

        self.assertTrue(
            isinstance(arccosineX_prime.value0.value1.value0.value0, numberAST)
        )
        self.assertEqual(arccosineX_prime.value0.value1.value0.value0.value0, 1)

        self.assertTrue(
            isinstance(arccosineX_prime.value0.value1.value0.value1, powAST)
        )
        self.assertTrue(
            isinstance(arccosineX_prime.value0.value1.value0.value1.value0, variableAST)
        )
        self.assertEqual(
            arccosineX_prime.value0.value1.value0.value1.value0.value0, "x"
        )

        self.assertTrue(
            isinstance(arccosineX_prime.value0.value1.value0.value1.value1, numberAST)
        )
        self.assertEqual(arccosineX_prime.value0.value1.value0.value1.value1.value0, 2)

    def test_arctanX(self):
        arctanX = arctanAST(self.variableX)
        arctanX_prime = arctanX._diff()

        self.assertTrue(isinstance(arctanX_prime, divAST))

        self.assertTrue(isinstance(arctanX_prime.value0, numberAST))
        self.assertEqual(arctanX_prime.value0.value0, 1)

        self.assertTrue(isinstance(arctanX_prime.value1, addAST))
        self.assertTrue(isinstance(arctanX_prime.value1.value0, numberAST))
        self.assertEqual(arctanX_prime.value1.value0.value0, 1)

        self.assertTrue(isinstance(arctanX_prime.value1.value1, powAST))
        self.assertTrue(isinstance(arctanX_prime.value1.value1.value0, variableAST))
        self.assertEqual(arctanX_prime.value1.value1.value0.value0, "x")
        self.assertTrue(isinstance(arctanX_prime.value1.value1.value1, numberAST))
        self.assertEqual(arctanX_prime.value1.value1.value1.value0, 2)


if __name__ == "__main__":
    unittest.main()
