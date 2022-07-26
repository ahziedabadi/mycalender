"""
sample tests 
"""


from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """test the calc ."""

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)