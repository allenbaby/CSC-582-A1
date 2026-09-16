"""Verify the abstract gate's storage and immediate-update contract."""

import pytest

from FourBitAdder.intern.AbstractDevice import AbstractDevice
from FourBitAdder.intern.AbstractGate import AbstractGate


class RecordingGate(AbstractGate):
    """Observe setter dispatch without implementing a logic-gate primitive."""

    def __init__(self) -> None:
        """Initialize the call record before constructing the gate pins."""
        self.calls = []
        super().__init__()

    def update(self) -> None:
        """Record the input state seen when the setter calls update()."""
        self.calls.append((self.in1, self.in2))


def test_abstract_gate_remains_abstract() -> None:
    """The gate inherits the device contract and requires an update override."""
    assert issubclass(AbstractGate, AbstractDevice)
    with pytest.raises(TypeError):
        AbstractGate()


def test_construction_initializes_pins_without_updating() -> None:
    """All pins start at zero and construction does not trigger recomputation."""
    gate = RecordingGate()
    assert gate.getIn1() == 0
    assert gate.getIn2() == 0
    assert gate.getOut() == 0
    assert gate.calls == []
    assert gate.repr() == "in1: 0, in2: 0, out: 0"


def test_each_setter_updates_after_storing_input() -> None:
    """Both setters dispatch immediately, including when a bit is unchanged."""
    gate = RecordingGate()
    expected_calls = []
    for a in (0, 1):
        for b in (0, 1):
            previous_b = gate.getIn2()
            gate.setIn1(a)
            expected_calls.append((a, previous_b))
            assert gate.calls == expected_calls
            assert gate.getIn1() == a

            gate.setIn2(b)
            expected_calls.append((a, b))
            assert gate.calls == expected_calls
            assert gate.getIn2() == b
            assert gate.repr() == f"in1: {a}, in2: {b}, out: 0"
