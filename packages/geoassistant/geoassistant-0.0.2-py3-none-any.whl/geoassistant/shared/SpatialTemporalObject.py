from typing import Optional

from geoassistant.shared.SpatialObject import SpatialObject
from geoassistant.shared.TemporalObject import TemporalObject


class SpatialTemporalObject(SpatialObject, TemporalObject):

    SpatialObject.extendFactories(TemporalObject.getFieldsFactories())

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

