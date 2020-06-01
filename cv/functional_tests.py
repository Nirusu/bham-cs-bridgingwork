from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_retrieve_cv_homepage(self):
        # A Fortune 500 company has heard that Nils is a top web developer.
        # They want to check out his CV, so they check it out at this page.
        self.browser.get('http://localhost:8000/cv')

        # Since they keep open everyone's CV at once, they have to check out the title in their on how's CV they're looking at.
        # Putting all the shitty ones aside, Nils' CV definitely looks like a gold mine and someone they definitely have to hire.
        self.assertIn("Nils' CV", self.browser.title)


if __name__ == '__main__':
    unittest.main()
