"""Build a two-input XOR exclusively by wiring five primitive gates."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.LogicGates import AND, NAND, OR


class Xor2(AbstractDevice):
    """Combine two NAND inverters, two AND gates, and one OR gate."""

    def __init__(self) -> None:
        """Create the component gates and settle the zero-valued inputs."""
        self.a = 0
        self.b = 0
        self.out = 0
        self.not_a = NAND(1)
        self.not_b = NAND(2)
        self.a_not_b = AND(3)
        self.not_a_b = AND(4)
        self.combine = OR(5)
        self.update()

    def setA(self, value: int) -> None:
        """Set input A (0 or 1), then recompute the output before returning."""
        self.a = value
        self.update()

    def setB(self, value: int) -> None:
        """Set input B (0 or 1), then recompute the output before returning."""
        self.b = value
        self.update()

    def getA(self) -> int:
        """Return input A."""
        return self.a

    def getB(self) -> int:
        """Return input B."""
        return self.b

    def getOut(self) -> int:
        """Return the settled XOR output bit."""
        return self.out

    def update(self) -> None:
        """Propagate inputs through inverters, AND gates, then the OR gate."""
        self.not_a.setIn1(self.a)
        self.not_a.setIn2(self.a)
        self.not_b.setIn1(self.b)
        self.not_b.setIn2(self.b)
        self.a_not_b.setIn1(self.a)
        self.a_not_b.setIn2(self.not_b.getOut())
        self.not_a_b.setIn1(self.not_a.getOut())
        self.not_a_b.setIn2(self.b)
        self.combine.setIn1(self.a_not_b.getOut())
        self.combine.setIn2(self.not_a_b.getOut())
        self.out = self.combine.getOut()
