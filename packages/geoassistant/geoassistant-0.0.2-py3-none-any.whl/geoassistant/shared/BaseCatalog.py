import csv
import datetime
from abc import ABC, abstractmethod

from typing import Optional, Type, Dict, List, Any, TypeVar, Generic, Literal, TYPE_CHECKING, Union

import numpy as np
from typing_extensions import Tuple

from geoassistant.shared.BaseObject import BaseObject

if TYPE_CHECKING:
    from geoassistant.shared.BaseCollection import BaseCollection

CollectionType = TypeVar('CollectionType', bound='BaseCollection')
ElementType = TypeVar('ElementType', bound='BaseObject')


class BaseCatalog(BaseObject, ABC, Generic[CollectionType, ElementType]):

    def __init__(self,
                 filepath: str,
                 name: Optional[str] = None):
        super().__init__(name=name)

        self.filepath: str = filepath

        self.fields_attributes: Dict[str, Optional[Tuple]] = {field: None for field in
                                                              self.getElementClass().getFieldsFactories().keys()}
        self.fields_attributes['Name'] = None

        self.catalog_data: Optional[Dict[str, List[Any]]] = None

        self.elements_collection: CollectionType = self.getCollectionClass()()

        self.readFile()

    def __len__(self) -> int:
        return len(self.elements_collection)

    def __getitem__(self, identifier: Union[int, str]) -> ElementType:
        return self.elements_collection[identifier]

    def __str__(self) -> str:
        txt = (f"{self.__class__.__name__}("
               f"filepath='{self.filepath}', "
               f"elements={len(self.elements_collection):,}, "
               f"variables={len(self.catalog_data)})")
        return txt

    def getVariablesKeys(self) -> List[str]:
        return list(self.catalog_data.keys())

    def getFirstDataLine(self) -> str:
        with open(self.filepath, mode='r') as file:
            file.readline()
            return file.readline()

    def getElements(self) -> CollectionType:
        return self.elements_collection

    @abstractmethod
    def getElementClass(self) -> Type: ...

    @abstractmethod
    def getCollectionClass(self) -> Type: ...

    def setNameAttributes(self, key: str) -> None:
        self.fields_attributes['Name'] = (key, None)
        for i, el in enumerate(self.elements_collection):
            el.setName(name=self.catalog_data[key][i])

    def setPositionAttributes(self, xkey: str, ykey: str, zkey: str, units: Literal['m']) -> None:
        self.fields_attributes['Position'] = ((xkey, ykey, zkey), units)
        for i, el in enumerate(self.elements_collection):
            try:
                x = float(self.catalog_data[xkey][i])
                y = float(self.catalog_data[ykey][i])
                z = float(self.catalog_data[zkey][i])
                pos = np.array([x, y, z])
            except ValueError:
                pos = None

            el.setPosition(value=pos, units=units)

    def setDatetimeAttributes(self, key: str, date_format: str) -> None:
        self.fields_attributes['Datetime'] = (key, date_format)
        for i, el in enumerate(self.elements_collection):
            try:
                dt = datetime.datetime.strptime(self.catalog_data[key][i], date_format)
            except ValueError:
                dt = self.catalog_data[key][i]
            el.setDatetime(value=dt)

    def readFile(self) -> None:
        with open(self.filepath, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)

            self.catalog_data = {field_key: [] for field_key in header}

            for row in reader:
                self.elements_collection.addElement(element=self.getElementClass()())
                for i, fk in enumerate(header):
                    self.catalog_data[fk] += [row[i]]
