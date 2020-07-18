"""
AbideObject is the most basic of the useful Abide classes.

Most, if not all, persisted objects should subclass from AbideObject.
"""

from abide import base
from abide import properties

class AbideObject(base.AbideBase):
    id_key = ('name',)
    name = properties.StringProperty(
        help="Unique name for this object.",
        required=True
    )
