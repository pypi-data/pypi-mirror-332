from typing import Optional, Literal, TYPE_CHECKING, Union, List

import numpy as np

if TYPE_CHECKING:
    from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryMetrics import ExplicitGeometryMetrics


class ExplicitGeometryProperties(object):

    def __init__(self):
        super().__init__()

        self.nodes: Optional[np.ndarray] = None

        self.explicit_metrics: Optional['ExplicitGeometryMetrics'] = None

    def setNodes(self, nodes: Union[List, np.ndarray]) -> None:
        if isinstance(nodes, list):
            nodes = np.array(nodes)
        self.nodes = nodes
        self.explicit_metrics.calculateMetrics()

    def resetNodes(self) -> None:
        """
        Without reseting metrics.
        Used when transforming into external library objects (e.g. trimesh).
        """
        self.nodes = None

    def getNodes(self) -> Optional[np.ndarray]:
        return self.nodes

    def getDimensions(self) -> Optional[Literal[2, 3]]:
        return self.explicit_metrics.getDimensions()

    def getLimits(self) -> Optional[np.ndarray]:
        return self.explicit_metrics.getLimits()

    def getCenter(self) -> Optional[np.ndarray]:
        return self.explicit_metrics.getCenter()
