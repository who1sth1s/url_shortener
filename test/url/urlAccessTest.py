import unittest

from service.url.urlAccess import UrlAccess


class UrlStatsTest(unittest.TestCase):

    def setUp(self):
        self.request = {
            'method': 'GET'
        }

    def fail_test_get(self):
        url_number = 1223123
        result = UrlAccess(self.request, url_number).execute()
        self.assertEqual(result.get('error') is not None, True)

    def success_test_get(self):
        url_number = 7
        result = UrlAccess(self.request, url_number).execute()
        self.assertEqual(result.get('registered_url') is not None, True)

if __name__ == '__main__':
    unittest.main()
