# -*- coding: utf-8 -*-
"""
Abide
~~~~~
Abide is a Python library for creating enhanced objects which can easily be
serialized, persisted, and manipulated.

Currently DynamoDB is the supported persistence backend.

Example usage:
   >>> import abide
   >>> from abide import properties
   >>>
   >>> class MyObject(abide.NamedClass):
   >>>    properties = [
   >>>       properties.StringProperty(
   >>>          'str_val',
   >>>          default = "123",
   >>>          help = "A nice string value"
   >>>       )
   >>>    ]
   >>>
   >>> o = MyObject(name="useful_object")
   >>> print(o)
   MyObject(name="useful_object",stl_val=123)
   >>> print(o.str_val)
   "123"
   >>> o.save()    # All properties will be sent and saved into DynamoDB
   >>>
   >>> n = MyObject.load(name = "useful_object")
   >>> print(n)
   MyObject(name="useful_object")
   >>> n == o
   True
   >>> n.str_val="abc"
   >>> print(n)
   MyObject(name="useful_object", str_val = "abc")
   >>> n == o
   False
   >>> n.update()   # Only changed values (in this case, str_val) will be sent.

:copyright: (c) 2018 by Kyle Petersen.
:license: Apache 2.0, see LICENSE.md for more details.
"""
