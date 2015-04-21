"""
test for source.lab2round1orc.py
"""

from unittest import TestCase
# from source.lab2round1orc import Orc
from source.lab2round1orc import get_orc_distance
from source.lab2round1orc import get_orc_velocity
from source.lab2round1orc import get_orc_id
from source.lab2round1orc import remove_orc
from source.lab2round1orc import set_orc_id
from source.lab2round1orc import get_orc_by_id
from source.lab2round1orc import get_orc_type

import logging

logger = logging.getLogger(__name__)
logging.getLogger().setLevel(__debug__)


class TestOrc (TestCase):

    def test_get_orc_distance(self):
        # orc = Orc(100, 50, 2)
        result = get_orc_distance(100)
        self.assertEqual(result, 100)

    def test_get_orc_velocity(self):
        # orc = Orc(100, 50, 2)
        result = get_orc_velocity(50)
        self.assertEqual(result, 50)

    def test_get_orc_type(self):
        # orc = Orc(100, 50, 2)
        result = get_orc_type(2)
        self.assertEqual(result, 2)

    def test_get_orc_id(self):
        # orc = Orc(100, 50, 2)
        result = get_orc_id(3)
        self.assertEqual(result, 3)

    def test_remove_orc(self):
        # orc = Orc(100, 50, 2)
        result = remove_orc()
        self.assertEqual(result, False)

    def test_set_orc_id(self):
        # orc = Orc(100, 50, 2)
        result = set_orc_id(5)
        self.assertEqual(result, 5)

    def test_get_orc_by_id(self):
        # orc = Orc(100, 50, 2)
        result = get_orc_by_id(23)
        self.assertEqual(result, 23)