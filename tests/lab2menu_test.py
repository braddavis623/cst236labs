"""
test for lab2menu.py
"""

from unittest import TestCase
from source.lab2menu import do_something

import logging

logger = logging.getLogger(__name__)
logging.getLogger().setLevel(__debug__)      # added logging for requirement 2 of round 1


class TestCommands(TestCase):

    def test_do_something_quit(self):
        result = do_something('X')
        self.assertEqual(result, 'quitting')

    def test_do_something_give_options(self):
        result = do_something('?')
        self.assertEqual(result, 'giving options')

    def test_do_something_demo_capabilities(self):
        result = do_something('d')
        self.assertEqual(result, 'generating orc listing..')

    def test_do_something_auto_win(self):
        result = do_something('ENTer the trees')
        self.assertEqual(result, 'you win')

