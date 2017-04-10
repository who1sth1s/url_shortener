import unittest

from service.url.urlStats import UrlStats


class UrlStatsTest(unittest.TestCase):

    def setUp(self):
        self.request = {
            'method': 'GET'
        }

    def fail_test_get(self):
        url_number = 1223123
        result = UrlStats(self.request, url_number).execute()
        self.assertEqual(result[1], 400)

    def success_test_get(self):
        url_number = 7
        result = UrlStats(self.request, url_number).execute()
        self.assertEqual(result[1], 200)

if __name__ == '__main__':
    unittest.main()
