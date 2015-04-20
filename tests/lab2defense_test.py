"""
test for lab2defense.py
"""

from unittest import TestCase
from source.lab2defense import detect_breached
import logging

logger = logging.getLogger(__name__)
loging.getLogger().setLevel(__debug__)      # added logging for requirement 2 of round 1


class TestDefense(testcase):

    def test_detect_breached_breached(self):
        result = detect_breached(90, 100)
        self.assertEqual(result, True)

    def test_detect_breached_not_breached(self):
        result = detect_breached(110, 100)
        self.assertEqual(result, False)
