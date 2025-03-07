import datetime
from typing import Optional

from geoassistant.shared.BaseObject import BaseObject
from geoassistant.shared.BaseRecord import BaseRecord
from geoassistant.shared.BaseRecordsFactory import BaseRecordsFactory


class TemporalObject(BaseObject):

    BaseObject.extendFactories({
        'Datetime': BaseRecordsFactory(field_name='Datetime', expected_type=datetime.datetime, expected_units=None),
    })

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.datetime: Optional[BaseRecord] = None

    def setDatetime(self, value: datetime.datetime) -> None:
        self.datetime = self.fields_factories['Datetime'].create(value=value)

    def getDatetime(self) -> Optional[datetime.datetime]:
        return self.datetime.getValue()
