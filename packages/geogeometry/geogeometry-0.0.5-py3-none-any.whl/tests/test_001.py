import unittest
from geogeometry import Triangulation, Vector, Rotations, Plane


class TestBaseGeometry(unittest.TestCase):

    def setUp(self):
        pass

    def test_triangulation_creation(self):
        t = Triangulation()
        self.assertIsNotNone(t)
        self.assertIsInstance(t, Triangulation)

    def test_vectors_rotations(self):
        v1 = Vector(tip=[0., 0., 1.])
        v2 = Vector(tip=[0, 1, 0])

        R = Rotations.calculateRotationMatrixFromVectors(v0=v1, v1=v2)

        v1.rotateByRotationMatrix(R)

        self.assertEqual(v1, v2)

    def test_planes_creation(self):
        test_vector = Vector(tip=[1, 0, 0])

        p = Plane.createFromThreePoints(n0=[0, 0, 0], n1=[0, 1, 0], n2=[0, 0, 1])
        self.assertEqual(p.getNormalVector(), test_vector)

        p = Plane.createFromDipAndDipdir(origin=[0, 0, 0], dip=90., dipdir=90.)
        self.assertEqual(p.getNormalVector(), test_vector)

        p = Plane.createAsOrthogonal(axis='x', level=500.)
        self.assertEqual(p.getNormalVector(), test_vector)

        p = Plane.createAsVerticalProjection(n0=[0, 0], n1=[0, 1])
        self.assertEqual(p.getNormalVector(), test_vector)


if __name__ == "__main__":
    unittest.main()
