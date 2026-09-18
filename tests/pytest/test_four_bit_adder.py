"""Exercise the public entry point and all 512 four-bit additions."""

from FourBitAdder.FourBitAdder import FourBitAdder
from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.FullAdder import FullAdder


def test_construction_and_composition() -> None:
    """The public class starts at zero and owns four distinct full-adders."""
    adder = FourBitAdder()
    assert isinstance(adder, AbstractDevice)
    assert (adder.getA(), adder.getB(), adder.getCin()) == (0, 0, 0)
    assert (adder.getSum(), adder.getCout()) == (0, 0)
    assert len(adder.stages) == 4
    assert len({id(stage) for stage in adder.stages}) == 4
    for stage in adder.stages:
        assert isinstance(stage, FullAdder)


def test_all_512_additions() -> None:
    """Compare every operand/carry combination with independent integer addition."""
    adder = FourBitAdder()
    for a in range(16):
        for b in range(16):
            for cin in range(2):
                adder.setA(a)
                adder.setB(b)
                adder.setCin(cin)
                expected = a + b + cin
                assert (adder.getA(), adder.getB(), adder.getCin()) == (a, b, cin)
                assert adder.getSum() == expected % 16, (a, b, cin)
                assert adder.getCout() == expected // 16, (a, b, cin)
                assert adder.getCout() * 16 + adder.getSum() == expected


def test_each_input_setter_from_every_starting_state() -> None:
    """Check immediate results when each input changes or is set unchanged."""
    adder = FourBitAdder()
    for a in range(16):
        for b in range(16):
            for cin in range(2):
                adder.setA(a)
                adder.setB(b)
                adder.setCin(cin)
                for setter, changed, original in (
                    (adder.setA, 15 - a, a),
                    (adder.setB, 15 - b, b),
                    (adder.setCin, 1 - cin, cin),
                ):
                    for value in (changed, changed, original):
                        setter(value)
                        expected = adder.getA() + adder.getB() + adder.getCin()
                        assert adder.getSum() == expected % 16
                        assert adder.getCout() == expected // 16


def test_carry_propagates_through_all_four_stages() -> None:
    """Adding carry-in to 1111 ripples to cout, and removing it clears carries."""
    adder = FourBitAdder()
    adder.setA(15)
    adder.setCin(1)
    assert (adder.getSum(), adder.getCout()) == (0, 1)
    for stage in adder.stages:
        assert (stage.getA(), stage.getB(), stage.getCin()) == (1, 0, 1)
        assert (stage.getSum(), stage.getCout()) == (0, 1)
    adder.setCin(0)
    assert (adder.getSum(), adder.getCout()) == (15, 0)
    for stage in adder.stages:
        assert (stage.getCin(), stage.getSum(), stage.getCout()) == (0, 1, 0)


def test_instances_do_not_share_components_or_pins() -> None:
    """Changing one adder leaves a separately constructed adder at zero."""
    first = FourBitAdder()
    second = FourBitAdder()
    first.setA(15)
    first.setB(15)
    first.setCin(1)
    assert (first.getSum(), first.getCout()) == (15, 1)
    assert (second.getA(), second.getB(), second.getCin()) == (0, 0, 0)
    assert (second.getSum(), second.getCout()) == (0, 0)
