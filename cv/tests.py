from datetime import datetime

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User

from .models import AboutMe, EducationEntry, WorkEntry, Skills, Interests
from .views import cv_show


# Create your tests here.


class CvTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")

    def test_cv_url_resolves_to_cv_homepage(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_show)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_show(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn("<title>Nils' CV</title>", html)
        self.assertTrue(html.endswith('</html>'))

    # Test creation / edit / remove for each form
    # How to make tests dependent? Could make separate tests this way without duplicate code...
    def test_aboutme_form_create(self):
        response = self.client.post('/cv/aboutme/new/',
                                    data={"name": "Test Name", "dob": "01/01/1970", "email": "test@test.com",
                                          "location": "Germany", "text": "Hey I'm a cool guy, please hire me."},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AboutMe.objects.count(), 1)
        new_item = AboutMe.objects.first()
        self.assertEqual(new_item.text, "Hey I'm a cool guy, please hire me.")

    def test_aboutme_form_edit(self):
        response = self.client.post('/cv/aboutme/new/',
                                    data={"name": "Test Name", "dob": "01/01/1970", "email": "test@test.com",
                                          "location": "Germany", "text": "Hey I'm a cool guy, please hire me."},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AboutMe.objects.count(), 1)
        new_item = AboutMe.objects.first()
        self.assertEqual(new_item.text, "Hey I'm a cool guy, please hire me.")

        response = self.client.post('/cv/aboutme/1/edit/',
                                    data={"name": "Test Name", "dob": "01/01/1970", "email": "test@test.com",
                                          "location": "Germany", "text": "Hey I'm a bad guy, please don't hire me."},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AboutMe.objects.count(), 1)
        new_item = AboutMe.objects.first()
        self.assertEqual(new_item.text, "Hey I'm a bad guy, please don't hire me.")

    def test_aboutme_delete(self):
        response = self.client.post('/cv/aboutme/new/',
                                    data={"name": "Test Name", "dob": "01/01/1970", "email": "test@test.com",
                                          "location": "Germany", "text": "Hey I'm a cool guy, please hire me."},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AboutMe.objects.count(), 1)

        response = self.client.get('/cv/aboutme/1/remove/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AboutMe.objects.count(), 0)

    def test_education_form_create(self):
        response = self.client.post('/cv/education/new/',
                                    data={"title": "IT Security Student", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Ruhr University Bochum",
                                          "text": "I was the best student ever, haha."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(EducationEntry.objects.count(), 1)
        new_item = EducationEntry.objects.first()
        self.assertEqual(new_item.title, "IT Security Student")
        self.assertEqual(new_item.fromDate, datetime(2016, 1, 1).date())
        self.assertEqual(new_item.fromDateShown, "Oct 2016")
        self.assertEqual(new_item.toDate, datetime(2020, 9, 30).date())
        self.assertEqual(new_item.toDateShown, "Sep 2020")
        self.assertEqual(new_item.company, "Ruhr University Bochum")
        self.assertEqual(new_item.text, "I was the best student ever, haha.")

    def test_education_form_edit(self):
        response = self.client.post('/cv/education/new/',
                                    data={"title": "IT Security Student", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Ruhr University Bochum",
                                          "text": "I was the best student ever, haha."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(EducationEntry.objects.count(), 1)
        new_item = EducationEntry.objects.first()
        self.assertEqual(new_item.title, "IT Security Student")
        self.assertEqual(new_item.fromDate, datetime(2016, 1, 1).date())
        self.assertEqual(new_item.fromDateShown, "Oct 2016")
        self.assertEqual(new_item.toDate, datetime(2020, 9, 30).date())
        self.assertEqual(new_item.toDateShown, "Sep 2020")
        self.assertEqual(new_item.company, "Ruhr University Bochum")
        self.assertEqual(new_item.text, "I was the best student ever, haha.")

        response = self.client.post('/cv/education/1/edit/',
                                    data={"title": "IT Security Student", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Ruhr University Bochum",
                                          "text": "I was the worst student ever, haha."}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(EducationEntry.objects.count(), 1)
        self.assertEqual(EducationEntry.objects.count(), 1)
        new_item = EducationEntry.objects.first()
        self.assertEqual(new_item.text, "I was the worst student ever, haha.")

    def test_education_form_delete(self):
        response = self.client.post('/cv/education/new/',
                                    data={"title": "IT Security Student", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Ruhr University Bochum",
                                          "text": "I was the best student ever, haha."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(EducationEntry.objects.count(), 1)

        response = self.client.get('/cv/education/1/remove/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(EducationEntry.objects.count(), 0)

    def test_work_form_create(self):
        response = self.client.post('/cv/work/new/',
                                    data={"title": "Test Employee", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Test Company",
                                          "text": "I was the best employee ever, haha."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(WorkEntry.objects.count(), 1)
        new_item = WorkEntry.objects.first()
        self.assertEqual(new_item.title, "Test Employee")
        self.assertEqual(new_item.fromDate, datetime(2016, 1, 1).date())
        self.assertEqual(new_item.fromDateShown, "Oct 2016")
        self.assertEqual(new_item.toDate, datetime(2020, 9, 30).date())
        self.assertEqual(new_item.toDateShown, "Sep 2020")
        self.assertEqual(new_item.company, "Test Company")
        self.assertEqual(new_item.text, "I was the best employee ever, haha.")

    def test_work_form_edit(self):
        response = self.client.post('/cv/work/new/',
                                    data={"title": "Test Employee", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Test Company",
                                          "text": "I was the best employee ever, haha."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(WorkEntry.objects.count(), 1)
        new_item = WorkEntry.objects.first()
        self.assertEqual(new_item.title, "Test Employee")
        self.assertEqual(new_item.fromDate, datetime(2016, 1, 1).date())
        self.assertEqual(new_item.fromDateShown, "Oct 2016")
        self.assertEqual(new_item.toDate, datetime(2020, 9, 30).date())
        self.assertEqual(new_item.toDateShown, "Sep 2020")
        self.assertEqual(new_item.company, "Test Company")
        self.assertEqual(new_item.text, "I was the best employee ever, haha.")

        response = self.client.post('/cv/work/1/edit/',
                                    data={"title": "Test Employee", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Test Company",
                                          "text": "I was the worst employee ever, haha."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(WorkEntry.objects.count(), 1)
        new_item = WorkEntry.objects.first()
        self.assertEqual(new_item.text, "I was the worst employee ever, haha.")

    def test_work_form_delete(self):
        response = self.client.post('/cv/work/new/',
                                    data={"title": "Test Employee", "fromDate": "01/01/2016",
                                          "fromDateShown": "Oct 2016", "toDate": "30/09/2020",
                                          "toDateShown": "Sep 2020", "company": "Test Company",
                                          "text": "I was the best employee ever, haha."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(WorkEntry.objects.count(), 1)

        response = self.client.get('/cv/work/1/remove/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(WorkEntry.objects.count(), 0)

    def test_skills_form_create(self):
        response = self.client.post('/cv/skills/new/', data={"skills": "Nothing, I'm useless."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Skills.objects.count(), 1)
        new_item = Skills.objects.first()
        self.assertEqual(new_item.skills, "Nothing, I'm useless.")

    def test_skills_form_edit(self):
        response = self.client.post('/cv/skills/new/', data={"skills": "Nothing, I'm useless."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Skills.objects.count(), 1)
        new_item = Skills.objects.first()
        self.assertEqual(new_item.skills, "Nothing, I'm useless.")

        response = self.client.post('/cv/skills/1/edit/', data={"skills": "Everything, I'm so talented."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Skills.objects.count(), 1)
        new_item = Skills.objects.first()
        self.assertEqual(new_item.skills, "Everything, I'm so talented.")

    def test_skills_form_delete(self):
        response = self.client.post('/cv/skills/new/', data={"skills": "Nothing, I'm useless."}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Skills.objects.count(), 1)

        response = self.client.get('/cv/skills/1/remove/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Skills.objects.count(), 0)

    def test_interests_form_create(self):
        response = self.client.post('/cv/interests/new/', data={"interests": "None, I don't have any hobbies."},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Interests.objects.count(), 1)
        new_item = Interests.objects.first()
        self.assertEqual(new_item.interests, "None, I don't have any hobbies.")

    def test_interests_form_edit(self):
        response = self.client.post('/cv/interests/new/', data={"interests": "None, I don't have any hobbies."},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Interests.objects.count(), 1)
        new_item = Interests.objects.first()
        self.assertEqual(new_item.interests, "None, I don't have any hobbies.")

        response = self.client.post('/cv/interests/1/edit/', data={"interests": "Football, Netflix"},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Interests.objects.count(), 1)
        new_item = Interests.objects.first()
        self.assertEqual(new_item.interests, "Football, Netflix")

    def test_interests_form_delete(self):
        response = self.client.post('/cv/interests/new/', data={"interests": "None, I don't have any hobbies."},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Interests.objects.count(), 1)

        response = self.client.get('/cv/interests/1/remove/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Interests.objects.count(), 0)