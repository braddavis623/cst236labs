"""
:mod:`source.lab2round1orc` -- Example source code
============================================

The following example code gives the distance  or velocity of an orc (arbitrary)
"""


class Orc:

    def __init__(self, d=0, v=0):
        self.velocity = v
        self.distance = d

    def get_orc_distance(self):
        """
        returns a distance for an orc

        :return: an int
        :rtype: int
        """
        return self.distance

    def get_orc_velocity(self):
        """
        returns a velocity for an orc

        :return: an int
        :rtype: int
        """
        return self.velocity