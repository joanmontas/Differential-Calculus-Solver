# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from differentiate import *

vari = variableAST("x")
numb3 = numberAST(3)
numb7 = numberAST(7)
sinX = sinAST(vari)
cosX = cosAST(vari)
x_pow_3 = powAST(vari, numb3)
sinX_pow_7 = powAST(sinX, numb7)
sin_x_pow_3 = sinAST(x_pow_3)

sinX_mult_cosX = multAST(sinX, cosX)
if __name__ == "__main__":
    # print(vari._diff())
    # print(numb3._diff())
    # print(sinX._diff())
    # print(cosX._diff())
    print(sinX_mult_cosX._diff())
    # print(sin_x_pow_3._diff())
    # print(sinX_pow_7._diff())