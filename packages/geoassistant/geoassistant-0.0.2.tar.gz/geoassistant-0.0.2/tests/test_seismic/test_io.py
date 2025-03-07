import datetime
import os
import unittest
from geoassistant import SeismicCatalog


class TestSeismicIO(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.resources_dir = os.path.join(self.base_dir, 'resources')

        self.catalog_001_path = os.path.join(self.resources_dir, "test_catalog_001.csv")

    def test_read_csv_catalog(self):
        sc = SeismicCatalog(filepath=self.catalog_001_path)

        sc.setPositionAttributes(xkey="LocX [m]", ykey="LocY [m]", zkey="LocZ [m]", units='m')

        sc.setDatetimeAttributes(key='#EventTime', date_format="%Y%m%d %H%M%S")
        sc.setMomentAttributes(key="Moment [Nm]", units='Nm')
        sc.setEnergyAttributes(key="Energy [J]", units='J')
        sc.setLocalMagnitudeAttributes(key="Local Magnitude")

        self.assertEqual(len(sc), 10)
        self.assertEqual(sc.getElements()[0].getLocalMagnitude(), -0.6)

        self.assertEqual(sc.getElements()[-1].getEnergy().getValue(), 16.3)
        self.assertEqual(sc.getElements()[-1].getEnergy().getUnits(), 'J')

        self.assertEqual(sc.getElements()[0].getDatetime(), datetime.datetime(year=2024, month=5, day=7, hour=2, minute=38, second=12))

        # events = sc.getEvents()
        # events.plotHazardCurve()
        # events = events.getSubsetWithinMagnitudes(lower_magnitude=-1.5, include_lower_limit=True)
        # events.plotGR(interval=0.1)


if __name__ == "__main__":
    unittest.main()
