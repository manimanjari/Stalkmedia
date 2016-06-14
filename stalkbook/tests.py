from django.test import TestCase


class StalkbookViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/home/')
        self.assertEqual(resp.status_code, 200)

    def test_valid_request(self):       
        resp = self.client.get('/images/?q=rome')
        self.assertEqual(resp.status_code, 200)
       
    def test_bad_request(self):
        resp = self.client.get('/images/?x=rome')
        self.assertEqual(resp.status_code, 400)
       
    def test_page_not_found(self):
        resp = self.client.get('/images/$')
        self.assertEqual(resp.status_code, 404)
