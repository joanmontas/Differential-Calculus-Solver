# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import unittest
from differentiate import *


class plainTrigonometricTest(unittest.TestCase):
    variableX = variableAST("x")

    def sinX_test(self):
        sinX = sinAST(variableX)
        sinX_prime = sinx._diff()
        self.assertTrue(isinstance(sinX_prime, cosAST))
        self.assertTrue(isinstance(sinX_prime.value0, variableAST))
        return


if __name__ == "__main__":
    print()
