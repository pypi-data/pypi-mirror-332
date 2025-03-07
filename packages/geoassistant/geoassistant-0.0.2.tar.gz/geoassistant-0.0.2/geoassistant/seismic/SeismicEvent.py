from typing import Literal, Optional

from geoassistant.shared.BaseRecord import BaseRecord
from geoassistant.shared.BaseRecordsFactory import BaseRecordsFactory
from geoassistant.shared.SpatialTemporalObject import SpatialTemporalObject


class SeismicEvent(SpatialTemporalObject):

    seismic_fields_factories = {
        'Moment': BaseRecordsFactory(field_name='Moment', expected_type=float, expected_units=['Nm']),
        'Energy': BaseRecordsFactory(field_name='Energy', expected_type=float, expected_units=['J', 'KJ', 'MJ']),
        'Local Magnitude': BaseRecordsFactory(field_name='Local Magnitude', expected_type=float, expected_units=None),
        'Frequency': BaseRecordsFactory(field_name='Frequency', expected_type=float, expected_units=['Hz'])
        # 'MomentP',
        # 'EnergyP',
        # 'MomentS',
        # 'EnergyS',
        # 'CornerFreq',
        # 'StaticStressDrop',
    }
    SpatialTemporalObject.extendFactories(seismic_fields_factories)

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.moment: Optional[BaseRecord] = None
        self.energy: Optional[BaseRecord] = None
        self.local_magnitude: Optional[BaseRecord] = None

        self.frequency: Optional[BaseRecord] = None  # Not corner-frequency. This is used in DSSD.

    def __str__(self) -> str:
        txt = (f"SeismicEvent("
               f"datetime={self.datetime.getValue()}, "
               f"position={self.position.getValue()}, "
               f"moment={self.moment.getValue():,} [{self.moment.getUnits()}], "
               f"energy={self.energy.getValue():,} [{self.energy.getUnits()}], "
               f"local_magnitude={self.local_magnitude.getValue():,} [-])")
        return txt

    def setMoment(self, value: float, units: Literal['Nm']) -> None:
        self.moment = self.getFieldsFactories()['Moment'].create(value=value, units=units)

    def setEnergy(self, value: float, units: Literal['J', 'KJ', 'MJ']) -> None:
        self.energy = self.getFieldsFactories()['Energy'].create(value=value, units=units)

    def setLocalMagnitude(self, value: float) -> None:
        self.local_magnitude = self.getFieldsFactories()['Local Magnitude'].create(value=value)

    def setFrequency(self, value: float, units: Literal['Hz']) -> None:
        self.frequency = self.getFieldsFactories()['Frequency'].create(value=value, units=units)

    def getMoment(self) -> Optional[BaseRecord]:
        return self.moment

    def getEnergy(self) -> Optional[BaseRecord]:
        return self.energy

    def getLocalMagnitude(self) -> Optional[float]:
        return self.local_magnitude.getValue()

    def getFrequency(self) -> Optional[BaseRecord]:
        return self.frequency