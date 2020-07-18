# -*- coding: utf-8 -*-
"""
abide.properties
~~~~~~~~~~~~~~~~
"""

from abide.utils import NotSet

class AbideProperty():
    """
    An AbideProperty defines the behavior of a named property of an Abide
    object. These properties may have the following defined:
    
    * name (string) - The name of this property.
    * required (bool) - If true, then the Abide object must have a value set
      for this property to pass validation.
    * default (object) - A default value to be used.
    * help (str) - Descriptive text.
    * aliases (iterable) - An iterable containing names to use as aliases. When
      an Abide object is stored, the property is stored under the "name" key,
      however the property may be referenced from the object using either name
      or alias.
    * transform (func) - An optional function to be called with the incoming
      value in order to transform it before storing.
    * override (object) - If set, will override any value in a hierarchy.
    * validation_callback (func) - An optional function to be called during
      object validation. Can be used to test the property and throw a
      validation exception if the property is to be considered invalid.
    """
    
    __slots__ = [
        '_name',
        '_required',
        '_default',
        '_help',
        '_aliases',
        '_transform',
        '_override',
        '_validation_callback',
    ]

    def __init__(self, *args, **kwargs):
        try:
            self._name = args[0]
        except IndexError:
            self._name = None
        self._required = kwargs.get('required', False)
        self._default = kwargs.get('default', NotSet)
        self._help = kwargs.get('help')
        self._aliases = kwargs.get('aliases')
        self._transform = kwargs.get('transform')
        self._override = kwargs.get('override', NotSet)
        self._validation_callback = kwargs.get('validation_callback')

    def __str__(self):
        return self.__class__.__name__ + '(name = ' + self.name + ')'

    @property
    def name(self):
        return self._name

    def get_instance(self):
        pass

    @classmethod
    def deserialize(cls, incoming):
        pass


class AbidePropertyInstance(object):
    
    __slots__ = [
        '_abide_object',
        '_abide_property',
        '_value',
        '_is_dirty',
        '_is_set',
    ]
    
    def __init__(self, abide_object, abide_property):
        self._abide_object = abide_object
        self._abide_property = abide_property
        self._is_dirty = False
        self._is_set = False
        pass
    
    def serialize(self):
        """Convert the property value into a form appropriate for persistence."""
        return str(self._value)


class StringProperty(AbideProperty):
    pass


class StringPropertyInstance(AbidePropertyInstance):
    pass
