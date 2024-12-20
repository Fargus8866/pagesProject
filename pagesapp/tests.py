from django.test import TestCase
from django.test import SimpleTestCase


# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code,200)

    def test_stajax_page_status_code(self):
        response = self.client.get('/stajax/')
        self.assertEqual(response.status_code,200)
