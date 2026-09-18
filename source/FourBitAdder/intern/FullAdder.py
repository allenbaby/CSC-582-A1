"""Compose two cascaded half-adders and an OR into a full-adder."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.HalfAdder import HalfAdder
from FourBitAdder.intern.LogicGates import OR


class FullAdder(AbstractDevice):
    """Add two input bits and a carry-in using only component wiring."""

    def __init__(self) -> None:
        """Create two independent half-adders and settle zero-valued pins."""
        self.a = 0
        self.b = 0
        self.cin = 0
        self.sum = 0
        self.cout = 0
        self.first = HalfAdder()
        self.second = HalfAdder()
        self.carry_gate = OR(1)
        self.update()

    def setA(self, value: int) -> None:
        """Set input A (0 or 1) and recompute outputs before returning."""
        self.a = value
        self.update()

    def setB(self, value: int) -> None:
        """Set input B (0 or 1) and recompute outputs before returning."""
        self.b = value
        self.update()

    def setCin(self, value: int) -> None:
        """Set carry-in (0 or 1) and recompute outputs before returning."""
        self.cin = value
        self.update()

    def getA(self) -> int:
        """Return input A."""
        return self.a

    def getB(self) -> int:
        """Return input B."""
        return self.b

    def getCin(self) -> int:
        """Return the carry-in bit."""
        return self.cin

    def getSum(self) -> int:
        """Return the settled sum bit."""
        return self.sum

    def getCout(self) -> int:
        """Return the settled carry-out bit."""
        return self.cout

    def update(self) -> None:
        """Settle the first half-adder, then the second, then combine carries."""
        self.first.setA(self.a)
        self.first.setB(self.b)
        self.second.setA(self.first.getSum())
        self.second.setB(self.cin)
        self.carry_gate.setIn1(self.first.getCarry())
        self.carry_gate.setIn2(self.second.getCarry())
        self.sum = self.second.getSum()
        self.cout = self.carry_gate.getOut()
