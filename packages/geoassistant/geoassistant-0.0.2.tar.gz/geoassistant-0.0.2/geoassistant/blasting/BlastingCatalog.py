from typing import Optional, Type

from geoassistant.shared.BaseCatalog import BaseCatalog

from geoassistant.blasting.BlastingEvent import BlastingEvent
from geoassistant.blasting.BlastingEventsCollection import BlastingEventsCollection


class BlastingCatalog(BaseCatalog[BlastingEventsCollection, BlastingEvent]):

    def __init__(self,
                 filepath: str,
                 name: Optional[str] = None):
        super().__init__(filepath=filepath, name=name)

    def getElementClass(self) -> Type:
        return BlastingEvent

    def getCollectionClass(self) -> Type:
        return BlastingEventsCollection
