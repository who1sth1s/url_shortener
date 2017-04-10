import unittest, ujson

from service.url.urlRegister import UrlRegister


class UrlRegisterTest(unittest.TestCase):

    def setUp(self):
        self.post_request = {
            'method': 'POST',
            'url': 'http://www.google.co.kr'
        }

    def test_post(self):
        result = UrlRegister(self.post_request).execute()
        print(ujson.loads(result))

    def test_get_duplicate_registered_url_method(self):
        result = UrlRegister(self.post_request)._get_duplicate_registered_url('http://www.vingle.net')
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
