from typing import Optional, Literal

import numpy as np

from geoassistant.shared.BaseObject import BaseObject
from geoassistant.shared.BaseRecord import BaseRecord
from geoassistant.shared.BaseRecordsFactory import BaseRecordsFactory


class SpatialObject(BaseObject):

    BaseObject.extendFactories({
        'Position': BaseRecordsFactory(field_name='Position', expected_type=np.ndarray, expected_units=['m'])
    })

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.position: Optional[BaseRecord] = None

    def setPosition(self, value: np.ndarray, units: Literal['m']) -> None:
        self.position = self.fields_factories['Position'].create(value=value, units=units)

    def getPosition(self) -> Optional[BaseRecord]:
        return self.position

    def calculateDistance(self, other_spatial_object: 'SpatialObject') -> Optional[BaseRecord]:
        """
        Calculates Euclidean distance between to spatial objects.
        :param other_spatial_object:
        :return: BaseRecord (value and units)
        """

        positions_meters = []
        positions_records = [self.position, other_spatial_object.getPosition()]
        for pr in positions_records:
            pos, units = pr.getValue(), pr.getUnits()
            if units != 'm':
                if units == 'km':
                    pos *= 1e3
                elif units == 'cm':
                    pos /= 1e2
            positions_meters += [pos]

        distance = np.linalg.norm(positions_meters[1]-positions_meters[0])

        record = BaseRecord(value=float(distance), units='m')
        return record

        # diff = self.position.getValue() - other_spatial_object.getPosition().getValue()
        # return np.linalg.norm(diff)
