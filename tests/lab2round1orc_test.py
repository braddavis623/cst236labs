"""
test for source.lab2round1orc.py
"""

from unittest import TestCase
from lab2round2orc import get_orc_distance
from lab2round2orc import get_orc_velocity
from lab2round2orc import get_orc_type

import logging

logger = logging.getLogger(__name__)
loging.getLogger().setLevel(__debug__)


class TestOrc (TestCase):

    def test_get_orc_distance(self):
        orc = Orc(100, 50, 2)
        result = get_orc_distance()
        self.assertEqual(result, 100)

    def test_get_orc_velocity(self):
        orc = Orc(100, 50, 2)
        result = get_orc_distance()
        self.assertEqual(result, 50)

    def test_get_orc_type(self):
        orc = Orc(100, 50, 2)
        result = get_orc_type()
        self.assertEqual(result, 2)

    def test_get_orc_id(self):
        orc = Orc(100, 50, 2)
        result = get_orc_id()
        self.assertEqual(result, get_orc_id())

    def test_remove_orc(self):
        orc = Orc(100, 50, 2)
        result = orc.remove_orc(orc.id)
        self.assertEqual(result, False)

    def test_set_orc_id(self):
        orc = Orc(100, 50, 2)
        result = set_orc_id(5)
        self.assertEqual(result, 5)