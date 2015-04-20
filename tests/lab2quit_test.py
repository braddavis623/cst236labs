"""
test for lab2quit.py
"""

from unittest import TestCase
from source.lab2quit import quit
import logging

logger = logging.getLogger(__name__)
loging.getLogger().setLevel(__debug__)      # added logging for requirement 2 of round 1


class TestDoQuit(testcase):

    def test_do_quit(self):
        result = do_quit('X')
        self.assertEqual(result, 'quitting')

