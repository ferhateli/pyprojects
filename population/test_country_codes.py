"""test module for the country codes module."""

import unittest
from country_codes import get_country_code


class CodesTestCase(unittest.TestCase):
    """Test for 'country_codes.py'."""

    def test_case_country(self):
        """Do upper case or lower case countries work?"""
        code = get_country_code('UNITED STATES')
        self.assertEqual(code, 'us')

unittest.main()
