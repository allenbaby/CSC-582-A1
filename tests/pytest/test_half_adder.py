"""Test half-adder construction, composition, and both output bits."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.HalfAdder import HalfAdder
from FourBitAdder.intern.LogicGates import AND
from FourBitAdder.intern.Xor2 import Xor2


def test_construction_and_composition() -> None:
    """A zero-initialized half-adder owns one XOR and one AND."""
    adder = HalfAdder()
    assert isinstance(adder, AbstractDevice)
    assert (adder.getA(), adder.getB(), adder.getSum(), adder.getCarry()) == (
        0,
        0,
        0,
        0,
    )
    assert isinstance(adder.xor, Xor2)
    assert isinstance(adder.carry_gate, AND)
    parts = [
        value for value in vars(adder).values() if isinstance(value, AbstractDevice)
    ]
    assert len(parts) == 2


def test_complete_truth_table_and_each_setter() -> None:
    """Exercise all four rows and check both outputs after each input change."""
    adder = HalfAdder()
    for a in (0, 1, 0):
        for b in (0, 1, 0):
            previous_b = adder.getB()
            adder.setA(a)
            assert adder.getSum() == (a + previous_b) % 2
            assert adder.getCarry() == (a + previous_b) // 2
            adder.setB(b)
            assert (adder.getA(), adder.getB()) == (a, b)
            assert adder.getSum() == (a + b) % 2
            assert adder.getCarry() == (a + b) // 2
