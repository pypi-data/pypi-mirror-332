import os
import tempfile
import unittest
from geogeometry import CadReader


class TestPlot3d(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.resource_dir = os.path.join(self.base_dir, '..', 'test_io', 'resources', 'dxf_files')

        self.file_006_path = os.path.join(self.resource_dir, "file_006.dxf")  # Mixed

    def test_file_006_V01(self):
        models_collection = CadReader.readFile(self.file_006_path)

        tmpfile = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        models_collection.plot2d(filepath=tmpfile.name)

        self.assertTrue(os.path.exists(tmpfile.name))

        tmpfile.close()
        if os.path.exists(tmpfile.name):
            os.remove(tmpfile.name)

    def test_file_006_V02(self):
        models_collection = CadReader.readFile(self.file_006_path)

        for plane in ['xy', 'yz', 'xz']:
            tmpfile = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
            models_collection.plot2d(filepath=tmpfile.name, projection_mode="3d", projection_plane=plane)

            self.assertTrue(os.path.exists(tmpfile.name))

            tmpfile.close()
            if os.path.exists(tmpfile.name):
                os.remove(tmpfile.name)


if __name__ == "__main__":
    unittest.main()
