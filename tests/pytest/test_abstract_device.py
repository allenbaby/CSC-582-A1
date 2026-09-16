"""Test the AbstractDevice base class contract."""

import pytest

from FourBitAdder.intern.AbstractDevice import AbstractDevice


def test_abstract_device_cannot_be_instantiated() -> None:
    """An abstract device cannot be instantiated without an update method."""
    with pytest.raises(TypeError):
        AbstractDevice()


def test_subclass_without_update_cannot_be_instantiated() -> None:
    """Inheritance alone does not fulfill the abstract update contract."""

    class IncompleteDevice(AbstractDevice):
        """Leave update abstract to check enforcement on subclasses."""

    with pytest.raises(TypeError):
        IncompleteDevice()


def test_concrete_subclass_can_implement_update() -> None:
    """A concrete override permits construction and dispatches through the base."""
    calls = []

    class ConcreteDevice(AbstractDevice):
        """Record update calls without introducing circuit behavior or pins."""

        def update(self) -> None:
            """Record that this subclass's update implementation was called."""
            calls.append("updated")

    device: AbstractDevice = ConcreteDevice()
    device.update()

    assert calls == ["updated"]
