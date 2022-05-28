# test_with_unittest.py

from unittest import TestCase
from nsetools import Nse

class TestMain(TestCase):
    def test_nsetools(self):
        self.assertIsNotNone(Nse().get_index_quote("nifty 50"))
