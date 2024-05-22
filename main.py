# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from differentiate import *

variableX = variableAST("x")
numb3 = numberAST(3)
numb7 = numberAST(7)
sinX = sinAST(variableX)
cosX = cosAST(variableX)
x_pow_3 = powAST(variableX, numb3)
sinX_pow_7 = powAST(sinX, numb7)
sin_x_pow_3 = sinAST(x_pow_3)
pow_sin_x_7 = powAST(sinAST(variableX), numb7)
tanX = tanAST(variableX)
sinX_mult_cosX = multAST(sinX, cosX)
sec2X = sec2AST(variableX)
cscX = cscAST(variableX)
csc2X = csc2AST(variableX)
arcsin = arcsineAST(variableX)
arctan = arctanAST(variableX)
tan_sinX = tanAST(sinX)
sec2_xPow3 = sec2AST(x_pow_3)
sec_sinX = secAST(sinX)
csc_XPow3 = cscAST(x_pow_3)
cot_XPow3 = cotAST(x_pow_3)
csc2_XPow3 = csc2AST(x_pow_3)
arcsin_xPow3 = arcsineAST(x_pow_3)
arccos_xPow3 = arccosineAST(x_pow_3)
arctan_xPow3 = arctanAST(x_pow_3)
ln_xPow3 = naturalLogAST(x_pow_3)

if __name__ == "__main__":
    # print(variableXableX._diff())
    # print(numb3._diff())
    # print(sinX._diff())
    # print(cosX._diff())
    # print(sinX_mult_cosX._diff())
    # print(sin_x_pow_3._diff())
    # print(sinX_pow_7._diff())
    # print(sin_x_pow_3._diff())
    # print(pow_sin_x_7._diff())
    # print(tanX._diff())
    # print(sec2X._diff())
    # print(cscX._diff())
    # print(csc2AST(variableX)._diff())
    # print(arcsin._diff())
    # print(arctan._diff())
    # print(tan_sinX._diff())
    # print(sec2_xPow3._diff())
    # print(sec_sinX._diff())
    # print(csc_XPow3._diff())
    # print(cot_XPow3._diff())
    # print(csc2_XPow3._diff())
    # print(arcsin_xPow3._diff())
    # print(arccos_xPow3._diff())
    # print(arctan_xPow3._diff())
    # print(ln_xPow3._diff())
    # print(f"The derivative of {divAST(numberAST(6), powAST(powAST(variableAST('z'), numberAST(3)), numberAST(0.5)))} is: ")
    # print(divAST(numberAST(6), powAST(powAST(variableAST("z"), numberAST(3)), numberAST(0.5)))._diff())
    # print(isAlgebraic(multAST(numb3, variableX)))
    # print(isAlgebraic(eulerAST()))
    # print(divAST(numb3, powAST(variableX, numb3))._diff())
    # print(powAST(eulerAST(), x_pow_3)._diff())
    # print(powAST(numb3, x_pow_3)._diff())
    # print(multAST(variableAST("x"), numberAST(4))._diff())
    # print(cscAST(variableAST("x"))._diff())
    # print(arcsinAST(variableAST("x"))._diff())
    print(csc2AST(variableAST("x"))._diff())
    print(powAST(cscAST(variableAST("x")), numberAST(2))._diff())