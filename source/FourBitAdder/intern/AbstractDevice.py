"""Define the abstract base class for FourBitAdder devices."""

from abc import ABC, abstractmethod


class AbstractDevice(ABC):
    """Define the shared output-update contract for gates and composite devices.

    Every input setter on a device must call update() so that its outputs
    reflect the current inputs before the setter returns. Subclasses provide
    their own pins and implement the recomputation for their device.

    This abstract base requires an update() implementation; each subclass
    is responsible for calling it from every input setter.
    """

    @abstractmethod
    def update(self) -> None:
        """Recompute outputs from current inputs before an input setter returns."""
        raise NotImplementedError
