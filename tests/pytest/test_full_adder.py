"""Verify full-adder construction and every three-bit input combination."""

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.FullAdder import FullAdder
from FourBitAdder.intern.HalfAdder import HalfAdder
from FourBitAdder.intern.LogicGates import OR


def test_construction_and_composition() -> None:
    """Start at zero with two distinct half-adders and one carry OR."""
    adder = FullAdder()
    assert isinstance(adder, AbstractDevice)
    assert (adder.getA(), adder.getB(), adder.getCin()) == (0, 0, 0)
    assert (adder.getSum(), adder.getCout()) == (0, 0)
    assert isinstance(adder.first, HalfAdder)
    assert isinstance(adder.second, HalfAdder)
    assert adder.first is not adder.second
    assert isinstance(adder.carry_gate, OR)
    parts = [
        value for value in vars(adder).values() if isinstance(value, AbstractDevice)
    ]
    assert len(parts) == 3


def test_complete_truth_table_and_each_setter() -> None:
    """Loop over all eight rows and check sum and carry after every setter."""
    adder = FullAdder()
    for a in (0, 1, 0):
        for b in (0, 1, 0):
            for cin in (0, 1, 0):
                for setter, value in (
                    (adder.setA, a),
                    (adder.setB, b),
                    (adder.setCin, cin),
                ):
                    setter(value)
                    expected = adder.getA() + adder.getB() + adder.getCin()
                    assert adder.getSum() == expected % 2
                    assert adder.getCout() == expected // 2
                assert (adder.getA(), adder.getB(), adder.getCin()) == (a, b, cin)
