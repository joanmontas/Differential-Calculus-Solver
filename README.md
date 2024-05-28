# Differential-Calculus-Solver
Targeting the Derivative Calculus Domain
# Grammar
    # <expression> := group
    #              | <unary>
    #              | <binary>
    #              | <terminal>

    # <group>     := LPAREN <expression> RPAREN
    #
    # <unary>     := MINUS <expression>

    # <binary>    := <expression> PLUS   <expression>
    #              | <expression> MINUS  <expression>
    #              | <expression> TIMES  <expression>
    #              | <expression> DIVIDE <expression>
    #              | <expression> POWER  <expression>
    #
    # <terminal>  := <variable>
    #              | <number>
    #              | <function>
    #              | <constant>
    #
    # <variable>  := [a-zA-Z]+
    # <number>    := d+
    # <constant>  := sin | cos | tan | ...
    # <function>  := <constant> group
