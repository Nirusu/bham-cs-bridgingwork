from django.urls import resolve
from django.test import TestCase
from .views import cv_show

# Create your tests here.

class HomePageTest(TestCase):

    def test_cv_url_resolves_to_cv_homepage(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_show)