"""test module for the hn_submissions script."""

import unittest


from hn_submissions import get_api_item


class HapiTestCase(unittest.TestCase):
    """Test class for get_api_item."""

    def test_case_http_response(self):
        """Test response for api calls."""
        apiobj = get_api_item(
            'https://hacker-news.firebaseio.com/v0/topstories.json'
            )
        self.assertEqual(apiobj.status_code, 200)

unittest.main()
