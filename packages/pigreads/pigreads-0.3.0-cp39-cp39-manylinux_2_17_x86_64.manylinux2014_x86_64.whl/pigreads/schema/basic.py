"""
Schema for some basic data types
--------------------------------
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Vector3D(BaseModel):
    """
    Vector in three dimensions in space.
    """

    x: float = 0
    "value in x direction"
    y: float = 0
    "value in y direction"
    z: float = 0
    "value in z direction"
    model_config = ConfigDict(extra="forbid")


class Slice(BaseModel):
    """
    Slice of an array.

    :see: :py:class:`slice`
    """

    axis: int = -1
    "axis of the slice"
    start: int | None = None
    "start of the slice"
    end: int | None = None
    "end of the slice"
    step: int | None = None
    "step of the slice"
    model_config = ConfigDict(extra="forbid")

    def __call__(self) -> slice:
        """
        Return a slice object.

        :return: slice object
        :see: :py:class:`slice`
        """
        return slice(self.start, self.end, self.step)
