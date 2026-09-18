"""Compose one XOR and one AND into a half-adder."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.LogicGates import AND
from FourBitAdder.intern.Xor2 import Xor2


class HalfAdder(AbstractDevice):
    """Produce sum and carry bits from two input bits using component objects."""

    def __init__(self) -> None:
        """Create the XOR and AND components and settle zero-valued pins."""
        self.a = 0
        self.b = 0
        self.sum = 0
        self.carry = 0
        self.xor = Xor2()
        self.carry_gate = AND(1)
        self.update()

    def setA(self, value: int) -> None:
        """Set input A (0 or 1) and recompute both outputs before returning."""
        self.a = value
        self.update()

    def setB(self, value: int) -> None:
        """Set input B (0 or 1) and recompute both outputs before returning."""
        self.b = value
        self.update()

    def getA(self) -> int:
        """Return input A."""
        return self.a

    def getB(self) -> int:
        """Return input B."""
        return self.b

    def getSum(self) -> int:
        """Return the settled sum bit."""
        return self.sum

    def getCarry(self) -> int:
        """Return the settled carry bit."""
        return self.carry

    def update(self) -> None:
        """Drive both components and copy their outputs to sum and carry."""
        self.xor.setA(self.a)
        self.xor.setB(self.b)
        self.carry_gate.setIn1(self.a)
        self.carry_gate.setIn2(self.b)
        self.sum = self.xor.getOut()
        self.carry = self.carry_gate.getOut()
