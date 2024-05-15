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
        if not isinstance(val0, int):
            raise TypeError("Error: numberAst expects an int as argumnt")
        self.value0 = val0

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

    def __str__(self):
        return f"sin({self.value0.__str__()})"

    def __type__(self):
        return self.nodeType

    def _diff(self):
        if self.value0.__type__() == "variable":
            return cosAST(self.value0)
        elif self.value0.__type__() == "number":
            return self
        elif self.value0.__type__() == "notdiff":
            return cosAST(self.value0._diff())
        else:
            return _chainRule(self)    


class cosAST(Ast):
    nodeType = "cos"

    def __init__(self, val0):
        self.value0 = val0

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
            raise NotImplementedError(
                "Error: cos's _diff condition not yet implemented."
            )


class negativeAST(Ast):
    nodeType = "negative"

    def __init__(self, val0):
        self.value0 = val0

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
            powerAST(self.value1, numberAST(2)),
        )


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
        if isinstance(self.value1, numberAST):
            n = self.value1.value0
            if isinstance(self.value0, variableAST):
                return multAST(numberAST(n), powAST(self.value0, numberAST(n - 1)))
            elif isinstance(self.value0, _notDiff):
                # Expresison that hold other expression inside should have a _notDiff as to not differentiate during chain rule
                return multAST(
                    numberAST(n), powAST(self.value0._diff(), numberAST(n - 1))
                )
            else:
                return _chainRule(self)


class _notDiff(Ast):
    nodeType = "notdiff"

    def __init__(self, val0):
        self.value0 = val0

    def __str__(self):
        return self.value0.__str__()

    def __type__(self):
        return self.nodeType

    def _diff(self):
        return self.value0


def _chainRule(f):
    if isinstance(f, powAST):
        print(f"f = {f}, f0 = {f.value1}")
        g = f.value0
        gPrime = g._diff()
        fPrime = powAST(_notDiff(g), f.value1)._diff()
        return multAST(fPrime, gPrime)
        # fPrime = powAST(variableAST(variableConstant), f.value0)
        # fPrime.value1 = g
        # print(fPrime)
    elif isinstance(f, sinAST):
        g = f.value0
        gPrime = g._diff()
        fPrime = sinAST(variableAST(variableConstant))._diff()
        fPrime.value0 = g
        return multAST(fPrime, gPrime)
    else:
        raise NotImplementedError(
            "Error: _chain rule is unable to acess this type's function g"
        )
