from django.test import TestCase


class StalkbookViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/home/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/images/$')
        self.assertEqual(resp.status_code, 404)
