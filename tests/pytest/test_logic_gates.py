"""Translate the starter's construction and exhaustive primitive-gate tests.

Expected outputs are fixed truth tables indexed by the two input bits, keeping
Boolean operations inside primitive update() implementations even in tests.
"""

import pytest

from FourBitAdder.intern.AbstractGate import AbstractGate
from FourBitAdder.intern.LogicGates import AND, NAND, OR

GATE_TABLES = (
    (AND, ((0, 0), (0, 1))),
    (NAND, ((1, 1), (1, 0))),
    (OR, ((0, 1), (1, 1))),
)


@pytest.mark.parametrize("gate_type", (AND, NAND, OR))
def test_construction(gate_type) -> None:
    """Every primitive starts with zero pins, including NAND's output."""
    gate = gate_type(1)
    assert isinstance(gate, AbstractGate)
    assert gate.getIn1() == 0
    assert gate.getIn2() == 0
    assert gate.getOut() == 0
    assert gate.repr() == f"id: 1{gate_type.__name__}, in1: 0, in2: 0, out: 0"


@pytest.mark.parametrize("gate_type, table", GATE_TABLES)
def test_complete_truth_table(gate_type, table) -> None:
    """Check every input combination using the starter's two-setter sequence."""
    gate = gate_type(1)
    for a in (0, 1):
        for b in (0, 1):
            gate.setIn1(a)
            gate.setIn2(b)
            assert gate.getIn1() == a
            assert gate.getIn2() == b
            assert gate.getOut() == table[a][b]
            assert gate.repr() == (
                f"id: 1{gate_type.__name__}, in1: {a}, in2: {b}, out: {table[a][b]}"
            )


@pytest.mark.parametrize("gate_type, table", GATE_TABLES)
def test_each_setter_recomputes_immediately(gate_type, table) -> None:
    """Check output before another setter can conceal a missed recomputation."""
    gate = gate_type(2)
    for fixed in (0, 1):
        gate.setIn2(fixed)
        for value in (0, 1, 1, 0):
            gate.setIn1(value)
            assert gate.getOut() == table[value][fixed]

        gate.setIn1(fixed)
        for value in (0, 1, 1, 0):
            gate.setIn2(value)
            assert gate.getOut() == table[fixed][value]


@pytest.mark.parametrize("setter_name", ("setIn1", "setIn2"))
def test_nand_zero_setter_triggers_first_update(setter_name: str) -> None:
    """Setting an unchanged zero input must change NAND's initial output to one."""
    gate = NAND(1)
    getattr(gate, setter_name)(0)
    assert gate.getOut() == 1


def test_nand_with_tied_inputs_behaves_as_not() -> None:
    """Drive both NAND inputs from each possible bit to obtain its inverse."""
    gate = NAND(1)
    expected = (1, 0)
    for value in (0, 1):
        gate.setIn1(value)
        gate.setIn2(value)
        assert gate.getOut() == expected[value]
