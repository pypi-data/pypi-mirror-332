class PolylinePlotProperties(object):

    def __init__(self):
        super().__init__()

        # 2D
        self.line_width: float = 2.
        self.line_style: str = '-'

        # 3D
        self.tube_radius: float = 1.

    def setLineWidth(self, line_width: float) -> None:
        self.line_width = line_width

    def setLineStyle(self, line_style: str) -> None:
        self.line_style = line_style

    def setTubeRadius(self, tube_radius: float) -> None:
        self.tube_radius = tube_radius

    def getLineWidth(self) -> float:
        return self.line_width

    def getLineStyle(self) -> str:
        return self.line_style

    def getTubeRadius(self) -> float:
        return self.tube_radius
