import unittest

from service.url.urlRegister import UrlRegister


class UrlRegisterTest(unittest.TestCase):

    def setUp(self):
        self.post_request = {
            'method': 'POST',
            'url': 'http://www.google.co.kr'
        }

    def test_post_duplicate_success(self):
        result = UrlRegister(self.post_request).execute()
        self.assertEqual(result[1], 200)

    def test_post_success(self):
        self.post_request['url'] = 'http://123.123.1213'
        result = UrlRegister(self.post_request).execute()
        self.assertEqual(result[1], 201)

    def test_get_duplicate_registered_url_method(self):
        result = UrlRegister(self.post_request)._get_duplicate_registered_url('http://www.vingle.net')
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
