"""Define the starter's two-input, one-output abstract gate contract."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice


class AbstractGate(AbstractDevice):
    """Store gate pins and recompute the output whenever either input is set.

    The inherited update() method remains abstract. The in1, in2, and out
    fields are intended for subclass use, matching the starter's protected
    fields; Python does not enforce protected access.
    """

    def __init__(self) -> None:
        """Initialize all three pins to zero without calling update()."""
        self.in1 = 0
        self.in2 = 0
        self.out = 0

    def setIn1(self, value: int) -> None:
        """Set input one to a bit (0 or 1) and immediately recompute output."""
        self.in1 = value
        self.update()

    def setIn2(self, value: int) -> None:
        """Set input two to a bit (0 or 1) and immediately recompute output."""
        self.in2 = value
        self.update()

    def getIn1(self) -> int:
        """Return the current value of input one."""
        return self.in1

    def getIn2(self) -> int:
        """Return the current value of input two."""
        return self.in2

    def getOut(self) -> int:
        """Return the current output pin value."""
        return self.out

    def repr(self) -> str:
        """Return the human-readable pin state specified by the starter."""
        return f"in1: {self.in1}, in2: {self.in2}, out: {self.out}"
