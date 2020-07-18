# -*- coding: utf-8 -*-
"""
abide.base
~~~~~~~~~~
"""

from abide.meta import AbideRegistered
from abide.properties import StringProperty
from abide import utils


class AbideBase(metaclass=AbideRegistered):
    storage=None
    id_key=None
    __instances=None
    _abide_base_class=StringProperty(help="Base class")

    def __new__(cls, *args, **kwargs):
        print(cls.__name__, "__new__", args, kwargs)
        new_obj = super().__new__(cls)
        new_obj._abide_base_class = utils.fully_qualified_class_name(cls)
        new_obj.__instances = {}
        return new_obj
    
    def __init__(self, *args, **kwargs):
        print(self.__class__.__name__, "__init__", args, kwargs)

    def load(self):
        pass

    def save(self, overwrite=False):
        pass

    def get_attribute(self):
        pass






#    def update(self):
#        pass

    def to_dict(self):
        pass

    def to_json(self):
        pass

    def to_yaml(self):
        pass

    def from_dict(self, incoming):
        pass

    def from_json(self, incoming):
        pass

    def from_yaml(self, incoming):
        pass

    @classmethod
    def my_check(cls, new_class):
        print("cls: ", cls)
        print("new_class: ", new_class)
        print("issubclass: ", issubclass(new_class, cls))

    @property
    def decorated(self):
        return 1

    @decorated.setter
    def decorated(self, val):
        self._decor = val

#    def __getitem__(self, key):
#        if key in self.property_registry:
#            
#        pass

    def __str__(self):
        st = '<{class_name} [{properties}]>'
        ptl = []
        for prop in self.property_registry:
            ptl.append(prop)
        s = st.format(class_name=self.__class__.__name__, properties=",".join(ptl))
        return s
