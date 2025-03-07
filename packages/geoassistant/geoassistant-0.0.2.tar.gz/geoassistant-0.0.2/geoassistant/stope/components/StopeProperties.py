from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geogeometry import Triangulation
    from geoassistant.stope.components.StopeRepresentation import StopeRepresentation


class StopeProperties(object):

    def __init__(self):
        self.representation: Optional['StopeRepresentation'] = None

    def setTriangulation(self, triangulation: 'Triangulation') -> None:
        self.representation.setTriangulation(triangulation=triangulation)

    def getTriangulation(self) -> Optional['Triangulation']:
        return self.representation.getTriangulation()

