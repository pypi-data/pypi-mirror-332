class BasePlotProperties(object):

    def __init__(self):
        super().__init__()

        self.color: str = 'red'
        self.opacity: float = 1.0

    def setColor(self, color: str) -> None:
        self.color = color

    def setOpacity(self, opacity: float) -> None:
        self.opacity = opacity

    def getColor(self) -> str:
        return self.color

    def getOpacity(self) -> float:
        return self.opacity
