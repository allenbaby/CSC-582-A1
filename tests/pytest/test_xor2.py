"""Test XOR construction, composition, and the complete truth table."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.LogicGates import AND, NAND, OR
from FourBitAdder.intern.Xor2 import Xor2


def test_construction_and_composition() -> None:
    """Start with zero pins and own precisely the required five primitives."""
    gate = Xor2()
    assert isinstance(gate, AbstractDevice)
    assert (gate.getA(), gate.getB(), gate.getOut()) == (0, 0, 0)
    parts = [
        value for value in vars(gate).values() if isinstance(value, AbstractDevice)
    ]
    assert sorted(type(part).__name__ for part in parts) == [
        "AND",
        "AND",
        "NAND",
        "NAND",
        "OR",
    ]
    assert len({id(part) for part in parts}) == 5
    assert isinstance(gate.not_a, NAND)
    assert isinstance(gate.not_b, NAND)
    assert isinstance(gate.a_not_b, AND)
    assert isinstance(gate.not_a_b, AND)
    assert isinstance(gate.combine, OR)


def test_complete_truth_table_and_each_setter() -> None:
    """Check all four rows and observe outputs immediately after each setter."""
    gate = Xor2()
    expected = ((0, 1), (1, 0))
    for a in (0, 1, 0):
        for b in (0, 1, 0):
            previous_b = gate.getB()
            gate.setA(a)
            assert gate.getOut() == expected[a][previous_b]
            gate.setB(b)
            assert (gate.getA(), gate.getB()) == (a, b)
            assert gate.getOut() == expected[a][b]
            assert (gate.not_a.getIn1(), gate.not_a.getIn2()) == (a, a)
            assert (gate.not_b.getIn1(), gate.not_b.getIn2()) == (b, b)
