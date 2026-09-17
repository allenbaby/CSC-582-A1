"""Provide AND, NAND, and OR: the system's only Boolean logic primitives.

Each gate starts with all pins at zero, as specified by the starter. Setting
either input triggers update(), including when the input value is unchanged.
NAND therefore produces one for zero inputs only after an update is triggered.
"""

from FourBitAdder.intern.AbstractGate import AbstractGate


class AND(AbstractGate):
    """Output one exactly when both input bits are one."""

    def __init__(self, idNumber: int) -> None:
        """Initialize zero-valued pins and the starter's numeric-prefix ID."""
        super().__init__()
        self.id = f"{idNumber}AND"

    def update(self) -> None:
        """Recompute the output using the primitive AND operation."""
        if self.in1 == 1 and self.in2 == 1:
            self.out = 1
        else:
            self.out = 0

    def repr(self) -> str:
        """Return the gate ID followed by the inherited pin representation."""
        return f"id: {self.id}, {super().repr()}"


class NAND(AbstractGate):
    """Output zero exactly when both input bits are one after recomputation."""

    def __init__(self, idNumber: int) -> None:
        """Initialize zero-valued pins and the starter's numeric-prefix ID."""
        super().__init__()
        self.id = f"{idNumber}NAND"

    def update(self) -> None:
        """Recompute the output using the primitive NAND operation."""
        if self.in1 == 1 and self.in2 == 1:
            self.out = 0
        else:
            self.out = 1

    def repr(self) -> str:
        """Return the gate ID followed by the inherited pin representation."""
        return f"id: {self.id}, {super().repr()}"


class OR(AbstractGate):
    """Output one when at least one input bit is one."""

    def __init__(self, idNumber: int) -> None:
        """Initialize zero-valued pins and the starter's numeric-prefix ID."""
        super().__init__()
        self.id = f"{idNumber}OR"

    def update(self) -> None:
        """Recompute the output using the primitive OR operation."""
        if self.in1 == 1 or self.in2 == 1:
            self.out = 1
        else:
            self.out = 0

    def repr(self) -> str:
        """Return the gate ID followed by the inherited pin representation."""
        return f"id: {self.id}, {super().repr()}"
