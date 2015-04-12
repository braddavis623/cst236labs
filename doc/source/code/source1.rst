Source Example
==============

Source1 provides functions for describing a triangle, as well as a rhombus.

Determining Triangle Type
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source1.get_triangle_type` provides users with a way to provide a set of three sides
of a triangle and returns the type of triangle ("equilateral", "isosceles", "scalene" or "invalid")

Scalene Example
^^^^^^^^^^^^^^^

>>> from source.source1 import get_triangle_type
>>> get_triangle_type(1, 2, 3)
'scalene'

Determining Rhombus Type
^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source1.get_rhombus_type` provides users with a way to provide a set of four sides
or angles of a rhombus and returns the type of rhombus ("square", "rectangle", "rhombus", "disconnected object",
or "invalid")

Square Example
^^^^^^^^^^^^^^^

>>> from source.source1 import get_rhombus_type
>>> get_rhombus_type(2, 2, 2, 2)
'square'


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source1
    :members: