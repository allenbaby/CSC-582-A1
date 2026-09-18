"""Public entry point for the virtual four-bit adder.

Import with ``from FourBitAdder.FourBitAdder import FourBitAdder``.
The class is re-exported from intern/ so callers use the required public module
without introducing a duplicate wrapper class or a second circuit instance.
"""

from FourBitAdder.intern.FourBitAdder import FourBitAdder

__all__ = ["FourBitAdder"]
