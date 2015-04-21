"""
:mod:`source.lab2round1orc` -- Example source code
============================================

The following example code gives the distance  or velocity of an orc (arbitrary)
"""
import random


class Orc:

    def __init__(self, d=0, v=0, t=1):
        self.velocity = v
        self.distance = d
        self.type = t
        self.id = random.randint(1, 100000)
        self.alive = True
        self.priority = 0

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

    def get_orc_type(self):
        """
        returns a type for an orc

        :return: an int
        :rtype: int
        """
        return self.type

    def get_orc_id(self):
        """
        returns an id for an orc

        :return: an int
        :rtype: int
        """
        return self.id

    def remove_orc(self, i=0):
        """
        changes the state of an orc so it can be removed

        :return: False
        :rtype: boolean
        """
        if self.id == i:
            self.alive = False
        return self.alive

    def set_orc_priority(self, p=0):
        """
        returns a priority for an orc

        :return: an int
        :rtype: int
        """
        self.priority = p
        return self.priority