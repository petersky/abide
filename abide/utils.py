"""
Utilities
"""

# Identity object indicating an attribute not set (primarily for use
# when None is a valid value).
NotSet = object()

def fully_qualified_class_name(cls):
    class_name = cls.__name__
    if cls.__module__ is not None and cls.__module__ != '__builtin__':
        class_name = '{}.{}'.format(cls.__module__, class_name)
    return class_name
