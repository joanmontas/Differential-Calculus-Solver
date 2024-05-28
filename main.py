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

    equation0 = "2 + 3 * 4"
    ast0 = s.parser.parse(equation0, lexer=l.lexer)
    print(f"d/dx {ast0} = {ast0._diff()}")

    equation1 = "(2 + 3) * 4"
    ast1 = s.parser.parse(equation1, lexer=l.lexer)
    print(f"d/dx {ast1} = {ast1._diff()}")
