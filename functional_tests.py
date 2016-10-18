import unittest
from selenium import webdriver


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Enigma', self.browser.title)


if __name__ == '__main__':
    unittest.main()
