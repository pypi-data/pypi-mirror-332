import copy
import gzip
import lzma
import pickle
from typing import Optional, TypeVar, Generic, Dict

from geoassistant.shared.base_components.BaseObjectProperties import BaseObjectProperties

ObjectType = TypeVar('ObjectType')


class BaseObject(BaseObjectProperties, Generic[ObjectType]):

    # Factories are used when dealing with expected known fields
    # Example 1: Moment or Energy for SeismicEvent
    # Example 2: RQD or FF for DrillholeInterval
    # Not used with generic data handlers like BlockModelField
    fields_factories = {}

    @classmethod
    def extendFactories(cls, new_factories: dict):
        cls.fields_factories = {**cls.fields_factories, **new_factories}

    @classmethod
    def getFieldsFactories(cls) -> Dict:
        return cls.fields_factories

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

    def copy(self):
        copy_p = copy.deepcopy(self)
        copy_p.setId(_id=id(copy_p))
        return copy_p

    # IO
    def save(self, savepath: str) -> None:
        if '.pkl.gz' in savepath:
            pickle.dump(self, gzip.open(savepath, 'wb'), pickle.HIGHEST_PROTOCOL)
        elif 'pkl.xz' in savepath:
            pickle.dump(self, lzma.open(savepath, 'wb'), pickle.HIGHEST_PROTOCOL)
        else:
            pickle.dump(self, open(savepath, 'wb'), pickle.HIGHEST_PROTOCOL)

        # print(f'{self.__class__.__name__} instance saved at: "' + savepath + '"')

    @staticmethod
    def load(load_path) -> ObjectType:
        if '.pkl.gz' in load_path:
            return pickle.load(gzip.open(load_path, 'rb'))
        elif 'pkl.xz' in load_path:
            return pickle.load(lzma.open(load_path, 'rb'))
        else:
            return pickle.load(open(load_path, 'rb'))
