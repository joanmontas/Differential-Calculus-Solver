# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from ply import yacc

from LexericalAnalysis import *
from SyntacticAnalysis import *
from Differentiator import *


if __name__ == "__main__":
    l = LexicalAnalyzer()
    s = SyntacticAnalyzer(l)

    equation = "3"
    ast = s.parser.parse(equation, lexer=l.lexer)
    print(ast)
