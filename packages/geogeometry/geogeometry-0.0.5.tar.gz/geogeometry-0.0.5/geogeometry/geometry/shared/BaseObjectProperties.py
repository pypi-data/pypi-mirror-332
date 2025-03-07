from typing import Optional, Literal

import numpy as np

from geogeometry.geometry.shared.BasePlotProperties import BasePlotProperties


class BaseObjectProperties(BasePlotProperties):

    def __init__(self, name: Optional[str] = None):
        super().__init__()

        self.name: Optional[str] = name
        self.id: int = id(self)

    def setName(self, name: str) -> None:
        self.name = name

    def setId(self, _id: int) -> None:
        self.id = _id

    def getName(self) -> str:
        return self.name

    def getId(self) -> int:
        return self.id

