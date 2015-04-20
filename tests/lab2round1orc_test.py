"""
test for source.lab2round1orc.py
"""

from unittest import TestCase
import logging

logger = logging.getLogger(__name__)
loging.getLogger().setLevel(__debug__)


class TestOrc (TestCase):

    def test_get_orc_distance(self):
        result = get_orc_distance(100)
        self.assertEqual(result, 100)

    def test_get_orc_velocity(self):
        result = get_orc_distance(100, 50)
        self.assertEqual(result, 50)