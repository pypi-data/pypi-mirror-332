from typing import Optional

from geoassistant.shared.BaseObject import BaseObject
from geoassistant.shared.SpatialTemporalObject import SpatialTemporalObject


class Stope(SpatialTemporalObject, StopeProperties):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

