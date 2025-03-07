from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geogeometry.geometry.block.Block import Block


class BlockMetrics(object):

    def __init__(self, block: 'Block'):
        self.block: 'Block' = block

        self.width: Optional[float] = None
        self.length: Optional[float] = None
        self.height: Optional[float] = None

    def getWidth(self) -> Optional[float]:
        return self.width

    def getLength(self) -> Optional[float]:
        return self.length

    def getHeight(self) -> Optional[float]:
        return self.height

    def calculateWidth(self, width: float) -> None:
        self.width = width

    def calculateLength(self, length: float) -> None:
        self.length = length

    def calculateHeight(self, height: float) -> None:
        self.height = height
