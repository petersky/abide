# -*- coding: utf-8 -*-
"""
abide.registry
~~~~~~~~~~~~~~
"""

class PropertyDoesNotExist(AttributeError):
    pass


class AbidePropertyRegistry():
    """
    Contains the properties that have been registered for persistence.
    
    When a Class is created, the 
    """
    
    def __init__(self, *args, **kwargs):
        self._property_references = {}
        self._property_instances = {}

    def __iter__(self):
        yield from self._property_references

    def __contains__(self, prop_name):
        return prop_name in self._property_references

    def __len__(self):
        return len(self._property_references)
    
    def items(self):
        yield from self._property_references.items()

    def set_property(self, prop):
        self._property_references[prop.name] = prop

    def get_property(self, prop_name):
        try:
            return self._property_references[prop_name]
        except KeyError:
            raise PropertyDoesNotExist(prop_name)

    def remove_property(self, prop_name):
        try:
            del self._property_references[prop_name]
        except KeyError:
            raise PropertyDoesNotExist(prop_name)

    def has_property(self, prop_name):
        return prop_name in self._property_references

    def create_instance(self, prop_name):
        pass

    def merge(self, registry):
        """
        Merge an existing AbideRegistry into this one, keeping properties
        already present in this one and only merging properties that don't
        yet exist.
        """
        for property_name, property_item in registry.items():
            if property_name not in self:
                self.set_property(property_item)
