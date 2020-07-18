# -*- coding: utf-8 -*-
"""
abide.meta
~~~~~~~~~~
"""

from abc import ABCMeta
from abide.properties import AbideProperty
from abide.registry import AbidePropertyRegistry


class AbideRegistered(ABCMeta):
    """
    Registry of Abide-derived classes.
    """
    
    def __new__(metacls, name, bases, namespace, **kwargs):
        property_registry = _construct_registry(namespace, bases)
        namespace['property_registry'] = property_registry
        new_class = super(AbideRegistered, metacls).__new__(metacls, name, bases, namespace, **kwargs)
        return new_class


def _construct_registry(namespace, bases):
    """
    Create the property registry object, first by iterating in reverse
    through bases to merge in existing registries, then by examining
    namespace for AbideProperties and/or a member named 'properties'.
    """
    registry = AbidePropertyRegistry()
    for base in reversed(bases):
        print("base:", base)
        if hasattr(base, 'property_registry'):
            print("base reg:", base.property_registry)
            registry.merge(base.property_registry)
    for (member_name, member) in list(namespace.items()):
        if isinstance(member, AbideProperty):
            member._name = member_name
            registry.set_property(member)
            del namespace[member_name]
    if 'properties' in namespace:
        try:
            for prop in namespace['properties']:
                registry.set_property(prop)
        except TypeError:
            pass
    return registry
