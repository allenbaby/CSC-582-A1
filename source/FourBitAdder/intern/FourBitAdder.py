"""Implement a four-stage ripple-carry adder behind the public entry point."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.FullAdder import FullAdder


class FourBitAdder(AbstractDevice):
    """Wire four full-adders with bit zero as the least significant bit.

    setA() and setB() accept unsigned four-bit integers (0 through 15), as in
    the starter test contract. Conversion to and from bit lists only encodes
    pin values: all sum and carry logic is performed by component objects.
    Input setters synchronously settle the entire circuit before returning.
    """

    def __init__(self) -> None:
        """Create four distinct full-adders and initialize all pins to zero."""
        self.a = [0, 0, 0, 0]
        self.b = [0, 0, 0, 0]
        self.cin = 0
        self.sum = [0, 0, 0, 0]
        self.cout = 0
        self.stages = [FullAdder() for _ in range(4)]
        self.update()

    def setA(self, value: int) -> None:
        """Encode operand A (0 through 15) as four pins and recompute outputs."""
        self.a = [int(bit) for bit in reversed(format(value, "04b"))]
        self.update()

    def setB(self, value: int) -> None:
        """Encode operand B (0 through 15) as four pins and recompute outputs."""
        self.b = [int(bit) for bit in reversed(format(value, "04b"))]
        self.update()

    def setCin(self, value: int) -> None:
        """Set the external carry-in (0 or 1) and recompute outputs."""
        self.cin = value
        self.update()

    def getA(self) -> int:
        """Read operand A's four pins as an unsigned integer."""
        return int("".join(str(bit) for bit in reversed(self.a)), 2)

    def getB(self) -> int:
        """Read operand B's four pins as an unsigned integer."""
        return int("".join(str(bit) for bit in reversed(self.b)), 2)

    def getCin(self) -> int:
        """Return the external carry-in bit."""
        return self.cin

    def getSum(self) -> int:
        """Read the four computed sum pins as an unsigned integer."""
        return int("".join(str(bit) for bit in reversed(self.sum)), 2)

    def getCout(self) -> int:
        """Return the carry-out of the most significant full-adder."""
        return self.cout

    def update(self) -> None:
        """Settle each stage from low bit to high bit, forwarding its carry."""
        carry = self.cin
        for index, stage in enumerate(self.stages):
            stage.setA(self.a[index])
            stage.setB(self.b[index])
            stage.setCin(carry)
            self.sum[index] = stage.getSum()
            carry = stage.getCout()
        self.cout = carry
