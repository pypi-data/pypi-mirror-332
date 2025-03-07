from typing import Optional, Union, List, Literal

import numpy as np

from geogeometry.geometry.shared.BaseObject import BaseObject

from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryProperties import ExplicitGeometryProperties
from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryMetrics import ExplicitGeometryMetrics
from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryTransformer import ExplicitGeometryTransformer


class ExplicitGeometry(BaseObject, ExplicitGeometryProperties):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.explicit_metrics: ExplicitGeometryMetrics = ExplicitGeometryMetrics(self)
        self.explicit_transformer: ExplicitGeometryTransformer = ExplicitGeometryTransformer(self)

    def calculateMetrics(self) -> None:
        self.explicit_metrics.calculateMetrics()  # Basic explicit metrics
        self.metrics.calculateMetrics()  # Custom defined metrics

    def translate(self, translation_vector: Union[List, np.ndarray]) -> None:
        self.explicit_transformer.translate(translation_vector=translation_vector)

    def rotateByRotationMatrix(self, rotation_matrix: np.ndarray) -> None:
        self.explicit_transformer.rotateByRotationMatrix(rotation_matrix=rotation_matrix)
