from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import cv_show

# Create your tests here.


class HomePageTest(TestCase):

    def test_cv_url_resolves_to_cv_homepage(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_show)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_show(request)
        html = response.content.decode('utf8')
        # New line because of the % load static % primitive in base.html
        self.assertTrue(html.startswith('\n<!doctype html>'))
        self.assertIn("<title>Nils' CV</title>", html)
        self.assertTrue(html.endswith('</html>'))
