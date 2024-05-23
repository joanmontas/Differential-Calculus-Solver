# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from ply import lex


class LexicalAnalyzer:
    def __init__(self):
        self.functions = {"sin": "SIN", "cos": "COS", "tan": "TAN"}
        self.constant = {"e": "EULER"}

        self.tokens = (
            (
                "NUMBER",
                "VARIABLE",
                "CONSTANT",
                "FUNCTION",
                "PLUS",
                "MINUS",
                "TIMES",
                "DIVIDE",
                "POWER",
                "LPAREN",
                "RPAREN",
            )
            + tuple(self.functions.values())
            + tuple(self.constant.values())
        )

        self.lexer = lex.lex(module=self)

    def t_IDENT(self, t):
        r"[a-zA-Z_]+"
        if t.value in self.functions:
            t.type = "FUNCTION"
        elif t.value in self.constant:
            t.type = "CONSTANT"
        else:
            t.type = "VARIABLE"
        self.test = t
        return t

    def t_NUMBER(self, t):
        r"\d+"
        t.value = int(t.value)
        return t

    def t_PLUS(self, t):
        r"\+"
        return t

    def t_MINUS(self, t):
        r"-"
        return t

    def t_TIMES(self, t):
        r"\*"
        return t

    def t_DIVIDE(self, t):
        r"/"
        return t

    def t_POWER(self, t):
        r"\^"
        return t

    def t_LPAREN(self, t):
        r"\("
        return t

    def t_RPAREN(self, t):
        r"\)"
        return t

    t_ignore = " \t"

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)


if __name__ == "__main__":
    l = LexicalAnalyzer()
    test_input = "(e ^ 2) + cos(x)"
    l.lexer.input(test_input)

    while True:
        token = l.lexer.token()
        if not token:
            break
        print(token)
