import unittest, ujson

from service.url.urlAccess import UrlAccess


class UrlStatsTest(unittest.TestCase):

    def test_get(self):
        request = {
            'method': 'GET'
        }
        url_number = 123123
        result = UrlAccess(request, url_number).execute()
        print(result)

if __name__ == '__main__':
    unittest.main()
