from selenium import webdriver
import unittest


class BrowserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_browser_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Enigma', self.browser.title)

if __name__ == '__main__':
    unittest.main()
