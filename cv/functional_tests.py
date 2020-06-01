from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    # Note: Most of the tests are designed as unit tests, as they require to be logged in and that's kind of
    # difficult to achieve with Selenium. So these tests mainly focus on the reader perspective, which is not much.

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_retrieve_cv_homepage(self):
        # A Fortune 500 company has heard that Nils is a top web developer.
        # They want to check out his CV, so they check it out at this page.
        self.browser.get('http://localhost:8000/cv')

        # Since they keep open everyone's CV at once, they have to check out the title in their on how's CV they're
        # looking at. Putting all the shitty ones aside, Nils' CV definitely looks like a gold mine and someone they
        # definitely have to hire.
        self.assertIn("Nils' CV", self.browser.title)

    def test_can_see_headlines(self):
        # Before they can hire what Nils has got going for them, they have to check each category
        self.browser.get('http://localhost:8000/cv')

        aboutme_element = self.browser.find_elements_by_class_name("aboutme")[0]
        self.assertIn("<h2>About Me</h2>", aboutme_element.get_attribute("innerHTML"))

        experience_element = self.browser.find_elements_by_class_name("experience")[0]
        self.assertIn("<h2>Experience</h2>", experience_element.get_attribute("innerHTML"))

        education_element = self.browser.find_elements_by_class_name("education")[0]
        self.assertIn("<h2>Education</h2>", education_element.get_attribute("innerHTML"))

        skills_element = self.browser.find_elements_by_class_name("skills")[0]
        self.assertIn("<h2>Skills</h2>", skills_element.get_attribute("innerHTML"))

        interests_element = self.browser.find_elements_by_class_name("interests")[0]
        self.assertIn("<h2>Interests</h2>", interests_element.get_attribute("innerHTML"))

    def test_has_meaningful_content(self):
        # The employer wants to check what Nils has achieved, so he should have written something about himself

        self.browser.get('http://localhost:8000/cv')

        aboutme_element = self.browser.find_elements_by_class_name("aboutme")[0]
        self.assertTrue(len(aboutme_element.text) > 30)

        experience_element = self.browser.find_elements_by_class_name("experience")[0]
        self.assertTrue(len(experience_element.text) > 30)

        education_element = self.browser.find_elements_by_class_name("education")[0]
        self.assertTrue(len(education_element.text) > 30)

        skills_element = self.browser.find_elements_by_class_name("skills")[0]
        self.assertTrue(len(skills_element.text) > 30)

        interests_element = self.browser.find_elements_by_class_name("interests")[0]
        self.assertTrue(len(interests_element.text) > 30)

    def test_cannot_access_form_without_login(self):
        # The employer wants to check if Nils is not a total goon when it comes to security.
        self.browser.get("http://localhost:8000/cv/aboutme/new/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/aboutme/1/edit/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/aboutme/1/remove/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/work/new/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/work/1/edit/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/work/1/remove/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/education/new/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/education/1/edit/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/education/1/remove/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/skills/new/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/skills/1/edit/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/skills/1/remove/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/interests/new/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/interests/1/edit/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

        self.browser.get("http://localhost:8000/cv/interests/1/remove/")
        self.assertIsNotNone(self.browser.find_element_by_id("id_password"))

    def test_can_see_login(self):
        self.browser.get("http://localhost:8000/cv")
        self.assertIsNotNone(self.browser.find_element_by_class_name("fa-sign-in-alt"))


'''
    def test_can_login(self):
        testuser = User.objects.create_user(username="test", password="test")
        self.browser.get("http://localhost:8000/accounts/login/?next=/cv/")
        username_input = self.browser.find_element_by_id("id_username")
        username_input.send_keys("test")
        password_input = self.browser.find_element_by_id("id_password")
        password_input.send_keys("test")
        password_input.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertIsNotNone(self.browser.get_cookie("sessionid"))
        testuser.delete()
'''

if __name__ == '__main__':
    unittest.main()
