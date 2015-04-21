"""
:mod:`source.lab2defense` -- Example source code
============================================

The following example code determines if the nearest orc is closer than the defense perimeter
"""


def detect_breached(a=0, b=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: OrcDistance
    :type a: int

    :param b: DefensePerimeter b
    :type b: int

    :return: True, False
    :rtype: boolean
    """
    if a < b:
        return True
    else:
        return False