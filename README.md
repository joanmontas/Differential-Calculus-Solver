# Differential-Calculus-Solver
Targeting the Derivative Calculus Domain

# Derivative Rules
### Basic Rules:
1. **Constant Rule**: $\frac{d}{dx}(c) = 0$
2. **Power Rule**: $\frac{d}{dx}(x^n) = nx^{n-1}$
3. **Sum Rule**: $\frac{d}{dx}(f(x) + g(x)) = \frac{d}{dx}(f(x)) + \frac{d}{dx}(g(x))$.
4. **Difference Rule**: $\frac{d}{dx}(f(x) - g(x)) = \frac{d}{dx}(f(x)) - \frac{d}{dx}(g(x))$.
5. **Product Rule**: $\frac{d}{dx}(f(x) \cdot g(x)) = f'(x) \cdot g(x) + f(x) \cdot g'(x)$.
6. **Quotient Rule**: $\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right) = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{(g(x))^2}$.

### Exponential and Logarithmic Functions:
7. **Exponential Function**: $\frac{d}{dx}(e^x) = e^x$.
8. **Natural Logarithm**: $\frac{d}{dx}(\ln(x)) = \frac{1}{x}$.

### Trigonometric Functions:
9. **Sine Function**: $\frac{d}{dx}(\sin(x)) = \cos(x)$.
10. **Cosine Function**: $\frac{d}{dx}(\cos(x)) = -\sin(x)$.
11. **Tangent Function**: $\frac{d}{dx}(\tan(x)) = \sec^2(x)$.

### Inverse Trigonometric Functions:
12. **Arcsine Function**: $\frac{d}{dx}(\arcsin(x)) = \frac{1}{\sqrt{1-x^2}}$.
13. **Arccosine Function**: $\frac{d}{dx}(\arccos(x)) = -\frac{1}{\sqrt{1-x^2}}$.
14. **Arctangent Function**: $\frac{d}{dx}(\arctan(x)) = \frac{1}{1+x^2}$.

### Chain Rule:
15. **Chain Rule**: If $y = f(g(x))$, then $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$, let $u = g(x)$.

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

# Reference
    https://www.eeweb.com/tools/calculus-derivatives-and-limits-reference-sheet/