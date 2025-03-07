from typing import TypeVar, Generic, Optional, List, Iterator, Union

from geoassistant.shared.BaseObject import BaseObject

CollectionType = TypeVar('CollectionType')
ElementType = TypeVar('ElementType', bound='BaseObject')


class BaseCollection(BaseObject[CollectionType], Generic[CollectionType, ElementType]):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.elements: List[ElementType] = []

    def __len__(self) -> int:
        return len(self.elements)

    def __iter__(self) -> Iterator[ElementType]:
        for e in self.elements:
            yield e

    def __getitem__(self, identifier: Union[int, str]) -> ElementType:
        if isinstance(identifier, int):
            return self.elements[identifier]
        else:
            for e in self.elements:
                if e.getName() == identifier:
                    return e
            else:
                raise ValueError(f"Element '{identifier}' not found in collection.")

    def __str__(self) -> str:
        txt = (f"{self.__class__.__name__}("
               f"elements={len(self.elements)})")
        return txt

    def addElement(self, element: ElementType) -> None:
        self.elements += [element]

    def deleteElement(self, identifier: Union[int, str]):
        if isinstance(identifier, int):
            self.elements.pop(identifier)
        else:
            for e in self.elements:
                if e.getName() == identifier:
                    self.elements.remove(e)
                    break
            else:
                raise ValueError(f"Element '{identifier}' not found in collection.")
