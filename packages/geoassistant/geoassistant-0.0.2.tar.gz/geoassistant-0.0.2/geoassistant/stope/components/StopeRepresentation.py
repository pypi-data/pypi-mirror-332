from typing import TYPE_CHECKING, Optional

from geogeometry import Triangulation, Block

if TYPE_CHECKING:
    from geoassistant.stope.Stope import Stope


class StopeRepresentation(object):

    def __init__(self, stope: 'Stope'):
        self.stope: 'Stope' = stope

        self.triangulation: Optional['Triangulation'] = None

    def setTriangulation(self, triangulation: 'Triangulation') -> None:
        self.triangulation = triangulation

    def getTriangulation(self) -> Optional['Triangulation']:
        return self.triangulation

    def createRepresentationFromBlock(self, block: 'Block') -> None:
        self.triangulation = block.getTriangulation()
