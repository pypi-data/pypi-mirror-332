from typing import TYPE_CHECKING, Optional

import numpy as np

from geogeometry import Polyline

if TYPE_CHECKING:
    from geogeometry.geometry.block.Block import Block
    from geogeometry.geometry.vector.Vector import Vector
    from geogeometry.geometry.polyline.PolylinesCollection import PolylinesCollection
    from geogeometry.geometry.triangulation.Triangulation import Triangulation


class BlockRepresentation(object):

    def __init__(self, block: 'Block'):
        self.block: 'Block' = block

        self.axis_vector: Optional['Vector'] = None  # Origin: n0

        self.wireframe: Optional['PolylinesCollection'] = None
        self.triangulation: Optional['Triangulation'] = None

    def getTriangulation(self) -> Optional['Triangulation']:
        return self.triangulation

    def createNodes(self) -> None:
        c0, c1 = self.block.getCorners()

        # Top face, clock-wise starting from c1
        n0 = c1
        n1 = [c1[0], c0[1], c1[2]]
        n2 = [c0[0], c0[1], c1[2]]
        n3 = [c0[0], c1[1], c1[2]]

        # Bot face, clock-wise starting from top-right xy corner
        n4 = [c1[0], c1[1], c0[2]]
        n5 = [c1[0], c0[1], c0[2]]
        n6 = c0
        n7 = [c0[0], c1[1], c0[2]]

        self.block.setNodes(nodes=np.array([n0, n1, n2, n3, n4, n5, n6, n7]))

    def createWireframe(self) -> None:
        segments = [
            [0, 1], [1, 2], [2, 3], [3, 0],  # Top segments
            [4, 5], [5, 6], [6, 7], [7, 4],  # Bot segments
            [0, 4], [1, 5], [2, 6], [3, 7],  # Vertical segments
        ]

        pc = PolylinesCollection()

        for s in segments:
            poly = Polyline(nodes=self.block.getNodes()[s])
            pc.addElement(element=poly)

        self.wireframe = pc

    def createTriangulation(self) -> None:
        faces = [
            [0, 1, 2], [0, 2, 3],  # TOP
            [1, 0, 5], [4, 5, 0],  # RIGHT
            [2, 1, 6], [6, 1, 5],  # FRONT
            [7, 2, 6], [2, 7, 3],  # LEFT
            [0, 3, 4], [4, 3, 7],  # BACK
            [4, 6, 5], [6, 4, 7],  # BOT
        ]

        faces = np.array(faces)

        self.triangulation = Triangulation()
        self.triangulation.setNodes(nodes=self.block.getNodes())
        self.triangulation.setFaces(faces=faces)
