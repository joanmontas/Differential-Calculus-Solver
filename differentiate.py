# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from abc import ABC, abstractmethod, ABCMeta

variableConstant = "x"


class MetaAst(ABCMeta):
    def __new__(cls, name, bases, attrs):
        # Check for the required attribute
        if "nodeType" not in attrs:
            raise TypeError("Concrete classes must define a 'nodeType'.")

        # Proceed with class creation
        return super().__new__(cls, name, bases, attrs)


class Ast(metaclass=MetaAst):
    nodeType = "AbstractNode"

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __type__(self):
        pass


class numberAST(Ast):
    nodeType = "number"

    def __init__(self, val0):
        if not isinstance(val0, int) and not isinstance(val0, float):
            raise TypeError("Error: numberAst expects an int as argumnt")
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return str(self.value0)

    def __type__(self):
        return self.nodeType

    def _diff(self):
        return "0"


class sinAST(Ast):
    nodeType = "sin"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"sin({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return cosAST(self.value0)
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class cosAST(Ast):
    nodeType = "cos"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"cos({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return negativeAST(sinAST(self.value0))
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class tanAST(Ast):
    nodeType = "tan"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"tan({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return sec2AST(self.value0)
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class sec2AST(Ast):
    nodeType = "sec2"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"sec2({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return multAST(
                numberAST(2), multAST(sec2AST(self.value0), tanAST(self.value0))
            )
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class secAST(Ast):
    nodeType = "sec"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"sec({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return multAST(secAST(self.value0), tanAST(self.value0))
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class cscAST(Ast):
    nodeType = "csc"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"csc({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return multAST(negativeAST(cscAST(self.value0)), cotAST(self.value0))
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class cotAST(Ast):
    nodeType = "cot"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"cot({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return negativeAST(csc2AST(self.value0))
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class csc2AST(Ast):
    nodeType = "csc2"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"csc2({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return multAST(
                negativeAST(numberAST(2)),
                multAST(cosAST(self.value0), csc2AST(self.value0)),
            )
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class arcsinAST(Ast):
    nodeType = "arcsin"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"sin^-1({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return divAST(
                numberAST(1),
                powAST(
                    subAST(numberAST(1), powAST(self.value0, numberAST(2))),
                    numberAST(0.5),
                ),
            )
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class arccosineAST(Ast):
    nodeType = "arccosine"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"cos^-1({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return negativeAST(
                divAST(
                    numberAST(1),
                    powAST(
                        subAST(numberAST(1), powAST(self.value0, numberAST(2))),
                        numberAST(0.5),
                    ),
                )
            )
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class arctanAST(Ast):
    nodeType = "arctan"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"tan^-1({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return divAST(
                numberAST(1), addAST(numberAST(1), powAST(self.value0, numberAST(2)))
            )
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class naturalLogAST(Ast):
    nodeType = "ln"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"ln({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        # NOTE(Joan) x must be > 0 - Joan
        if self.value0.__type__() == "variable":
            return divAST(numberAST(1), self.value0)
        elif self.value0.__type__() == "number":
            return self
        else:
            return _chainRule(self)


class negativeAST(Ast):
    nodeType = "negative"

    def __init__(self, val0):
        self.value0 = val0
        self.value1 = None

    def __str__(self):
        return f"(-({self.value0.__str__()}))"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return negativeAST(self.value0._diff())


class variableAST(Ast):
    nodeType = "variable"

    def __init__(self, val0):
        self.value0 = val0  # like x, y,...
        self.value1 = None

    def __str__(self):
        return str(self.value0)

    def __type__(self):
        return self.nodeType

    def _diff(self):
        return numberAST(0)


class addAST(Ast):
    nodeType = "add"

    def __init__(self, val0, val1):
        self.value0 = val0
        self.value1 = val1

    def __str__(self):
        return f"(({self.value0.__str__()}) + ({self.value1.__str__()}))"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        left = self.value0._diff()
        right = self.value1._diff()
        return addAST(left, right)


class subAST(Ast):
    nodeType = "sub"

    def __init__(self, val0, val1):
        self.value0 = val0
        self.value1 = val1

    def __str__(self):
        return f"(({self.value0.__str__()}) - ({self.value1.__str__()}))"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        left = self.value0._diff()
        right = self.value1._diff()
        return subAST(left, right)


class multAST(Ast):
    nodeType = "mult"

    def __init__(self, val0, val1):
        self.value0 = val0
        self.value1 = val1

    def __str__(self):
        return f"(({self.value0.__str__()}) * ({self.value1.__str__()}))"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        left = self.value0._diff()
        right = self.value1._diff()
        print(left, right, self.value0, self.value1)
        return addAST(multAST(left, self.value1), multAST(right, self.value0))


class divAST(Ast):
    nodeType = "div"

    def __init__(self, val0, val1):
        self.value0 = val0
        self.value1 = val1

    def __str__(self):
        return f"(({self.value0.__str__()}) / ({self.value1.__str__()}))"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        left = self.value0._diff()
        right = self.value1._diff()
        return divAST(
            subAST(multAST(left, self.value1), multAST(right, self.value0)),
            powAST(self.value1, numberAST(2)),
        )


class eulerAST(Ast):
    nodeType = "euler"

    def __init__(self):
        self.value0 = None
        self.value1 = None

    def __str__(self):
        return "e"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        return numberAST(0)


class powAST(Ast):
    nodeType = "pow"

    def __init__(self, val0, val1):
        self.value0 = val0
        self.value1 = val1

    def __str__(self):
        return f"(({self.value0.__str__()}) ^({self.value1.__str__()}) )"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        # NOTE(Joan) Power rule - Joan
        if isinstance(self.value1, numberAST):
            n = self.value1.value0
            if isinstance(self.value0, variableAST):
                return multAST(numberAST(n), powAST(self.value0, numberAST(n - 1)))
            elif isinstance(self.value0, eulerAST):
                return self
            else:
                return _chainRule(self)
        else:
            raise NotImplementedError(
                "Error: _chain rule is unable to acess this type's function g"
            )
        # TODO(Joan) acount of const^x - Joan
        # NOTE(Joan) x, could be a function itself, thus requires chain rule

        # TODO(Joan) acount of e^x - Joan
        # NOTE(Joan) x, could be a function itself, thus requires chain rule


# NOTE (Joan) Could simply implement this function inside the class - Joan
# NOTE (Joan) Or simply abstract functions with single variable and double variable and group them - Joan
def _chainRule(f):
    if isinstance(f, powAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = powAST(variableAST(variableConstant), f.value1)._diff()
        fPrime.value1.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, sinAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = sinAST(variableAST(variableConstant))._diff()
        fPrime.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, cosAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = cosAST(variableAST(variableConstant))._diff()
        fPrime.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, tanAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = tanAST(variableAST(variableConstant))._diff()
        fPrime.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, sec2AST):
        print(f"f = {f} f0 = {f.value0}")
        g = f.value0
        gPrime = g._diff()
        fPrime = sec2AST(variableAST(variableConstant))._diff()
        fPrime.value1.value1.value0 = g
        fPrime.value1.value0.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, secAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = secAST(variableAST(variableConstant))._diff()
        fPrime.value1.value0 = g
        fPrime.value0.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, cscAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = cscAST(variableAST(variableConstant))._diff()
        fPrime.value0.value0.value0 = g
        fPrime.value1.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, cotAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = cotAST(variableAST(variableConstant))._diff()
        print(fPrime)
        fPrime.value0.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, csc2AST):
        g = f.value0
        gPrime = g._diff()
        fPrime = csc2AST(variableAST(variableConstant))._diff()
        fPrime.value1.value0.value0 = g
        fPrime.value1.value1.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, arcsinAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = arcsinAST(variableAST(variableConstant))._diff()
        fPrime.value1.value0.value1.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, arccosineAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = arccosineAST(variableAST(variableConstant))._diff()
        fPrime.value0.value1.value0.value1.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, arctanAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = arctanAST(variableAST(variableConstant))._diff()
        fPrime.value1.value1.value0 = g
        return multAST(fPrime, gPrime)
    elif isinstance(f, naturalLogAST):
        print(f"f = {f} f0 = {f.value0}")
        g = f.value0
        gPrime = g._diff()
        fPrime = naturalLogAST(variableAST(variableConstant))._diff()
        fPrime.value1 = g
        return multAST(fPrime, gPrime)
    # TODO(Joan) a^x, e^x - Joan
    else:
        raise NotImplementedError(
            "Error: _chain rule is unable to acess this type's function g"
        )


def isAlgebraic(n):
    if not (isinstance(n, Ast)):
        return False
    if isinstance(n, variableAST):
        return True
    if isAlgebraic(n.value0):
        return True
    if isAlgebraic(n.value1):
        return True

    return False
