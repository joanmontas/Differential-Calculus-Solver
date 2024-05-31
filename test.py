# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import unittest
import random
from Differentiator import *
from LexericalAnalysis import *
from SyntacticAnalysis import *


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

    def test_sec2X(self):
        sec2X = sec2AST(self.variableX)
        sec2X_prime = sec2X._diff()

        self.assertTrue(isinstance(sec2X_prime, multAST))
        self.assertTrue(isinstance(sec2X_prime.value0, numberAST))
        self.assertEqual(sec2X_prime.value0.value0, 2)

        self.assertTrue(isinstance(sec2X_prime.value1, multAST))
        self.assertTrue(isinstance(sec2X_prime.value1.value0, sec2AST))
        self.assertTrue(isinstance(sec2X_prime.value1.value0.value0, variableAST))
        self.assertEqual(sec2X_prime.value1.value0.value0.value0, "x")

        self.assertTrue(isinstance(sec2X_prime.value1.value1, tanAST))
        self.assertTrue(isinstance(sec2X_prime.value1.value1.value0, variableAST))
        self.assertEqual(sec2X_prime.value1.value1.value0.value0, "x")

    def test_csc2X(self):
        csc2X = csc2AST(self.variableX)
        csc2X_prime = csc2X._diff()

        self.assertTrue(isinstance(csc2X_prime, negativeAST))
        self.assertTrue(isinstance(csc2X_prime.value0, multAST))

        self.assertTrue(isinstance(csc2X_prime.value0.value0, numberAST))
        self.assertEqual(csc2X_prime.value0.value0.value0, 2)

        self.assertTrue(isinstance(csc2X_prime.value0.value1, multAST))

        self.assertTrue(isinstance(csc2X_prime.value0.value1.value0, csc2AST))
        self.assertTrue(
            isinstance(csc2X_prime.value0.value1.value0.value0, variableAST)
        )
        self.assertEqual(
            csc2X_prime.value0.value1.value0.value0.value0, self.variableConstant
        )

        self.assertTrue(isinstance(csc2X_prime.value0.value1.value1, cotAST))
        self.assertTrue(
            isinstance(csc2X_prime.value0.value1.value1.value0, variableAST)
        )
        self.assertEqual(
            csc2X_prime.value0.value1.value1.value0.value0, self.variableConstant
        )


class plainEulerDifferentiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_eulerX(self):
        eulerX = powAST(eulerAST(), self.variableX)
        eulerX_prime = eulerX._diff()

        self.assertTrue(isinstance(eulerX_prime, powAST))

        self.assertTrue(isinstance(eulerX_prime.value0, eulerAST))

        self.assertTrue(isinstance(eulerX_prime.value1, variableAST))
        self.assertEqual(eulerX_prime.value1.value0, "x")


class plainNaturalLogDifferentiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_lnX(self):
        lnX = naturalLogAST(self.variableX)
        lnX_prime = lnX._diff()

        self.assertTrue(isinstance(lnX_prime, divAST))

        self.assertTrue(isinstance(lnX_prime.value0, numberAST))
        self.assertEqual(lnX_prime.value0.value0, 1)

        self.assertTrue(isinstance(lnX_prime.value1, variableAST))
        self.assertEqual(lnX_prime.value1.value0, "x")


class plainPowerRuleDifferentiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_xToThe1(self):
        xToThe1 = powAST(self.variableX, numberAST(1))
        xToThe1_prime = xToThe1._diff()

        self.assertTrue(isinstance(xToThe1_prime, multAST))

        self.assertTrue(isinstance(xToThe1_prime.value0, numberAST))
        self.assertEqual(xToThe1_prime.value0.value0, 1)

        self.assertTrue(isinstance(xToThe1_prime.value1, powAST))

        self.assertTrue(isinstance(xToThe1_prime.value1.value0, variableAST))
        self.assertEqual(xToThe1_prime.value1.value0.value0, "x")

        self.assertTrue(isinstance(xToThe1_prime.value1.value1, subAST))

        self.assertTrue(isinstance(xToThe1_prime.value1.value1.value0, numberAST))
        self.assertEqual(xToThe1_prime.value1.value1.value0.value0, 1)

        self.assertTrue(isinstance(xToThe1_prime.value1.value1.value1, numberAST))
        self.assertEqual(xToThe1_prime.value1.value1.value1.value0, 1)

    def test_xToTheEuler(self):
        xToTheEuler = powAST(self.variableX, eulerAST())
        xToTheEuler_prime = xToTheEuler._diff()

        self.assertTrue(isinstance(xToTheEuler_prime, multAST))

        self.assertTrue(isinstance(xToTheEuler_prime.value0, eulerAST))

        self.assertTrue(isinstance(xToTheEuler_prime.value1, powAST))

        self.assertTrue(isinstance(xToTheEuler_prime.value1.value0, variableAST))
        self.assertEqual(xToTheEuler_prime.value1.value0.value0, "x")

        self.assertTrue(isinstance(xToTheEuler_prime.value1.value1, subAST))

        self.assertTrue(isinstance(xToTheEuler_prime.value1.value1.value0, eulerAST))

        self.assertTrue(isinstance(xToTheEuler_prime.value1.value1.value1, numberAST))
        self.assertEqual(xToTheEuler_prime.value1.value1.value1.value0, 1)


class numberDifferetiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)
    numberOfTest = 10

    def test_postiveNumber(self):
        for i in range(0, self.numberOfTest):
            positiveNumber = random.randint(0, 9999999999)
            numberX = numberAST(positiveNumber)
            numberX_prime = numberX._diff()
            self.assertTrue(isinstance(numberX_prime, numberAST))
            self.assertEqual(numberX_prime.value0, 0)

    # NOTE() Negative numbers are negativeAst(numberAst(positive_constant))


class additionRuleDifferetiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_cosX_plus_sinX(self):
        cosX = cosAST(self.variableX)
        sinX = sinAST(self.variableX)

        cosXPlusSinX = addAST(cosX, sinX)

        cosXPlusSinX_prime = cosXPlusSinX._diff()

        self.assertTrue(isinstance(cosXPlusSinX_prime, addAST))

        self.assertTrue(isinstance(cosXPlusSinX_prime.value0, negativeAST))
        self.assertTrue(isinstance(cosXPlusSinX_prime.value0.value0, sinAST))

        self.assertTrue(isinstance(cosXPlusSinX_prime.value1, cosAST))


class substractionRuleDifferetiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_cosX_minus_sinX(self):
        cosX = cosAST(self.variableX)
        sinX = sinAST(self.variableX)

        cosXMinusSinX = subAST(cosX, sinX)

        cosXMinusSinX_prime = cosXMinusSinX._diff()

        self.assertTrue(isinstance(cosXMinusSinX_prime, subAST))

        self.assertTrue(isinstance(cosXMinusSinX_prime.value0, negativeAST))
        self.assertTrue(isinstance(cosXMinusSinX_prime.value0.value0, sinAST))

        self.assertTrue(isinstance(cosXMinusSinX_prime.value1, cosAST))


class multiplicationRuleDifferetiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_cosX_time_sinX(self):
        cosX = cosAST(self.variableX)
        sinX = sinAST(self.variableX)

        cosXMultSinX = multAST(cosX, sinX)

        cosXMultSinX_prime = cosXMultSinX._diff()

        self.assertTrue(isinstance(cosXMultSinX_prime, addAST))

        self.assertTrue(isinstance(cosXMultSinX_prime.value0, multAST))
        self.assertTrue(isinstance(cosXMultSinX_prime.value0.value0, negativeAST))
        self.assertTrue(isinstance(cosXMultSinX_prime.value0.value0.value0, sinAST))
        self.assertTrue(isinstance(cosXMultSinX_prime.value0.value1, sinAST))

        self.assertTrue(isinstance(cosXMultSinX_prime.value1, multAST))
        self.assertTrue(isinstance(cosXMultSinX_prime.value1.value0, cosAST))
        self.assertTrue(isinstance(cosXMultSinX_prime.value1.value1, cosAST))


class divisionRuleDifferetiation(unittest.TestCase):
    variableConstant = "x"
    variableX = variableAST(variableConstant)

    def test_cosX_dividedBy_sinX(self):
        cosX = cosAST(self.variableX)
        sinX = sinAST(self.variableX)

        cosXDivSinX = divAST(cosX, sinX)

        cosXDivSinX_prime = cosXDivSinX._diff()

        self.assertTrue(isinstance(cosXDivSinX_prime, divAST))

        self.assertTrue(isinstance(cosXDivSinX_prime.value0, subAST))

        self.assertTrue(isinstance(cosXDivSinX_prime.value0.value0, multAST))
        self.assertTrue(isinstance(cosXDivSinX_prime.value0.value0.value0, negativeAST))
        self.assertTrue(
            isinstance(cosXDivSinX_prime.value0.value0.value0.value0, sinAST)
        )
        self.assertTrue(isinstance(cosXDivSinX_prime.value0.value0.value1, sinAST))

        self.assertTrue(isinstance(cosXDivSinX_prime.value0.value1, multAST))
        self.assertTrue(isinstance(cosXDivSinX_prime.value0.value1.value0, cosAST))
        self.assertTrue(isinstance(cosXDivSinX_prime.value0.value1.value1, cosAST))

        self.assertTrue(isinstance(cosXDivSinX_prime.value1, powAST))

        self.assertTrue(isinstance(cosXDivSinX_prime.value1.value0, sinAST))

        self.assertTrue(isinstance(cosXDivSinX_prime.value1.value1, numberAST))
        self.assertEqual(cosXDivSinX_prime.value1.value1.value0, 2)


class syntaxNumber(unittest.TestCase):

    def test_positiveNumber(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber = random.randint(0, 9999999999)

        equation = str(positiveNumber)
        ast = s.parser.parse(equation, lexer=l.lexer)
        self.assertTrue(isinstance(ast, numberAST))
        self.assertEqual(ast.value0, positiveNumber)

    def test_negativeNumber(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber = random.randint(0, 9999999999)

        equation = "-" + str(positiveNumber)
        ast = s.parser.parse(equation, lexer=l.lexer)
        self.assertTrue(isinstance(ast, negativeAST))
        self.assertTrue(isinstance(ast.value0, numberAST))
        self.assertEqual(ast.value0.value0, positiveNumber)


class syntaxArithmetic(unittest.TestCase):

    def test_positivePositiveNumberAddition(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = str(positiveNumber0) + " + " + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, addAST))
        self.assertTrue(isinstance(ast.value0, numberAST))
        self.assertTrue(isinstance(ast.value1, numberAST))

    def test_positiveNegativeNumberAddition(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = str(positiveNumber0) + "+ -" + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, addAST))
        self.assertTrue(isinstance(ast.value0, numberAST))
        self.assertEqual(ast.value0.value0, positiveNumber0)

        self.assertTrue(isinstance(ast.value1, negativeAST))
        self.assertTrue(isinstance(ast.value1.value0, numberAST))
        self.assertEqual(ast.value1.value0.value0, positiveNumber1)

    def test_negativePositiveNumberAddition(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = "-" + str(positiveNumber0) + "+" + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, addAST))

        self.assertTrue(isinstance(ast.value0, negativeAST))
        self.assertTrue(isinstance(ast.value0.value0, numberAST))
        self.assertEqual(ast.value0.value0.value0, positiveNumber0)

        self.assertTrue(isinstance(ast.value1, numberAST))
        self.assertEqual(ast.value1.value0, positiveNumber1)

    def test_negativeNegativeNumberAddition(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = "-" + str(positiveNumber0) + "+ -" + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, addAST))

        self.assertTrue(isinstance(ast.value0, negativeAST))
        self.assertTrue(isinstance(ast.value0.value0, numberAST))
        self.assertEqual(ast.value0.value0.value0, positiveNumber0)

        self.assertTrue(isinstance(ast.value1, negativeAST))
        self.assertTrue(isinstance(ast.value1.value0, numberAST))
        self.assertEqual(ast.value1.value0.value0, positiveNumber1)

    def test_positivePositiveNumberSubstraction(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = str(positiveNumber0) + " - " + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, subAST))
        self.assertTrue(isinstance(ast.value0, numberAST))
        self.assertTrue(isinstance(ast.value1, numberAST))

    def test_positiveNegativeNumberSubstraction(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = str(positiveNumber0) + "- -" + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, subAST))
        self.assertTrue(isinstance(ast.value0, numberAST))
        self.assertEqual(ast.value0.value0, positiveNumber0)

        self.assertTrue(isinstance(ast.value1, negativeAST))
        self.assertTrue(isinstance(ast.value1.value0, numberAST))
        self.assertEqual(ast.value1.value0.value0, positiveNumber1)

    def test_negativePositiveNumberSubstraction(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = "-" + str(positiveNumber0) + "-" + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, subAST))

        self.assertTrue(isinstance(ast.value0, negativeAST))
        self.assertTrue(isinstance(ast.value0.value0, numberAST))
        self.assertEqual(ast.value0.value0.value0, positiveNumber0)

        self.assertTrue(isinstance(ast.value1, numberAST))
        self.assertEqual(ast.value1.value0, positiveNumber1)

    def test_negativeNegativeNumberSubstraction(self):
        l = LexicalAnalyzer()
        s = SyntacticAnalyzer(l)

        positiveNumber0 = random.randint(0, 9999999999)
        positiveNumber1 = random.randint(0, 9999999999)

        equation = "-" + str(positiveNumber0) + "- -" + str(positiveNumber1)

        ast = s.parser.parse(equation, lexer=l.lexer)

        self.assertTrue(isinstance(ast, subAST))

        self.assertTrue(isinstance(ast.value0, negativeAST))
        self.assertTrue(isinstance(ast.value0.value0, numberAST))
        self.assertEqual(ast.value0.value0.value0, positiveNumber0)

        self.assertTrue(isinstance(ast.value1, negativeAST))
        self.assertTrue(isinstance(ast.value1.value0, numberAST))
        self.assertEqual(ast.value1.value0.value0, positiveNumber1)

    def test_allTerminalAndBinaryOperation(self):

        # TODO(Joan) Add more terminals as needed - Joan
        terminals = [
            "sin(x)",
            "cos(x)",
            "tan(x)",
            "sec(x)",
            "csc(x)",
            "cot(x)",
            "arcsine(x)",
            "arccosine(x)",
            "arctan(x)",
            "e",
        ]

        binary_operators = ["+", "-", "/", "*", "^"]
        binary_operators_class_type = {
            "+": addAST,
            "-": subAST,
            "/": divAST,
            "*": multAST,
            "^": powAST,
        }

        for i in terminals:
            for j in terminals:
                for k in binary_operators:
                    l = LexicalAnalyzer()
                    s = SyntacticAnalyzer(l)

                    i_ast = s.parser.parse(i, lexer=l.lexer)
                    j_ast = s.parser.parse(j, lexer=l.lexer)

                    equation = f"{i} {k} {j}"

                    ast = s.parser.parse(equation, lexer=l.lexer)

                    self.assertTrue(isinstance(ast, binary_operators_class_type[k]))
                    self.assertTrue(isinstance(ast.value0, type(i_ast)))
                    self.assertTrue(isinstance(ast.value1, type(j_ast)))


if __name__ == "__main__":
    unittest.main()
