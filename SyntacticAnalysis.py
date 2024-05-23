# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from ply import yacc
from LexericalAnalysis import *
from Differentiator import *


class SyntacticAnalyzer:
    # TODO(Joan) Update grammar - Joan
    # <expression>  ::= <terminal>
    #                | '(' <expression> + <terminal> ')'
    #                | '(' <expression> - <terminal> ')'
    #                | '(' <expression> * <terminal> ')'
    #                | '(' <expression> / <terminal> ')'
    #                | '(' <expression> ^ <terminal> ')'
    # <terminal>    ::= <number> | <constant> | <function> | <constant> | '-' terminal
    # <number>      ::= d+
    # <const>       ::= e
    # <variable>    ::= [a-zA-Z]+
    # <function>    ::= <functionName> '(' <expression> ')'
    # <functionName>::= sin | cos | tan

    precedence = (
        ("left", "PLUS", "MINUS"),
        ("left", "TIMES", "DIVIDE"),
        ("right", "POWER"),
        ("right", "UMINUS"),
        ("left", "LPAREN", "RPAREN"),
    )

    def __init__(self, lexer):
        self.lex = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module=self)

    def p_expression(self, p):
        """expression : terminal
        | binary
        | unary
        | group
        """

        p[0] = p[1]

    def p_terminal(self, p):
        """terminal : variable
        | number
        | constant
        | function"""
        p[0] = p[1]

    def p_variable(self, p):
        """variable : VARIABLE"""
        p[0] = variableAST(p[1])

    def p_number(self, p):
        """number : NUMBER"""
        p[0] = numberAST(int(p[1]))

    def p_constant(self, p):
        """constant : CONSTANT"""
        # NOTE() Add more constant as needed
        if p[1] == "e":
            p[0] = eulerAST()
        else:
            self.er = f"ERROR: Syntax error at token {p}, unkown contant of type {p[2]}"
            yacc.errok

    def p_binary(self, p):
        """binary : expression PLUS expression
        | expression MINUS expression
        | expression TIMES expression
        | expression DIVIDE expression
        | expression POWER expression"""
        if p[2] == "+":
            p[0] = addAST(p[1], p[3])
        elif p[2] == "-":
            p[0] = subAST(p[1], p[3])
        elif p[2] == "*":
            p[0] = multAST(p[1], p[3])
        elif p[2] == "/":
            p[0] = divAST(p[1], p[3])
        elif p[2] == "^":
            p[0] = powAST(p[1], p[3])
        else:
            self.er = f"ERROR: Syntax error at token {p}, unkown binary of type {p[2]}"
            yacc.errok

    def p_unary(self, p):
        '''unary : MINUS expression %prec UMINUS'''
        p[0] = negativeAST(p[2])

    def p_group(self, p):
        '''group : LPAREN expression RPAREN'''
        p[0] = p[2]

    def p_function(self, p):
        '''function : FUNCTION group'''
        # NOTE() Add more function as needed
        if p[1] == "sin":
            p[0] = sinAST(p[2])
        elif p[1] == "cos":
            p[0] = cosAST(p[2])
        elif p[1] == "tan":
            p[0] = tanAST(p[2])
        else:
            self.er = (
                f"ERROR: Syntax error at token {p}, unkown function  of type {p[2]}"
            )
            yacc.errok

    def p_error(self, p):
        # TODO(Joan) Handle error - Joan
        print("Syntax error at token", p)
        self.er = f"Syntax error at token {p}"
        yacc.errok


if __name__ == "__main__":
    l = LexicalAnalyzer()
    s = SyntacticAnalyzer(l)

    # equation = "e"
    # equation = "x"
    # equation = "123"
    equation = "123 - e + 2"
    equation = "-2"
    equation = "x ^ (-2)"
    equation = "sin(-2)"
    equation = "x ^ -2 + 2"
    equation = "x ^ (-2 + 2)"
    equation = "(x ^ -2) + 2"
    equation = "cos(-2 + 2)"
    equation = "-4 * (-10)"

    ast = s.parser.parse(equation, lexer=l.lexer)
    print(ast)