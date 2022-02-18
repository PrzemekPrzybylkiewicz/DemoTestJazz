import unittest

from selenium import webdriver


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.base_url_produkt = 'https://autodemo.testoneo.com/en/' + "3-clothes"
        self.login_url = self.base_url + "login"
        self.sample_produkt_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r'C:\SE\chromedriver.exe')

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def assert_title_of_webpage(self, webpage, expected_title):
        driver = self.driver
        driver.get(webpage)
        title = driver.title
        self.assertEqual(title, expected_title, f'Expected title on page is {expected_title} at {driver.current_url}')


    def test_strona_glowna(self):
        webpage = self.base_url
        expected_title = "Lost Hat"
        self.assert_title_of_webpage(webpage, expected_title)

    def test_produkt(self):
        webpage = self.base_url_produkt
        expected_title = "Clothes"
        self.assert_title_of_webpage(webpage, expected_title)

    # rozwiazanie jaktestowa
    # def get_page_title(self, url):
    #     self.driver.get(url)
    #     return self.driver.title
    #
    # def asset_title(self, url, expected_title):
    #     actual_title = self.get_page_title(url)
    #     self.assertEqual(expected_title, actual_title,
    #                      f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')
