from typing import Optional


class BaseObjectProperties(object):

    def __init__(self, name: Optional[str] = None):
        super().__init__()

        self.name: Optional[str] = name
        self.description: Optional[str] = None

        self.id: int = id(self)

    def setName(self, name: str) -> None:
        self.name = name

    def setDescription(self, description: str) -> None:
        self.description = description

    def setId(self, _id: int) -> None:
        self.id = _id

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getId(self) -> int:
        return self.id
