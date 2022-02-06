import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import functional_helpers


class Mainautodemo(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + "login"
        self.sample_produkt_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r'C:\SE\chromedriver.exe')

    def tearDown(self):
        self.driver.close()

    def assert_element_text(self, driver, xpath, expected_text):
        header_element = driver.find_element(By.XPATH, xpath)
        header_element_text = header_element.text
        print(header_element_text)
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual on page:{driver.current_url}')

    def test_title_of_header(self):
        driver = self.driver
        driver.get(self.login_url)
        xpath = '//*[@id="main"]//h1'
        expected_text = 'Log in to your account'

        self.assert_element_text(driver, xpath, expected_text)



    def test_login_to_website(self):
        driver = self.driver
        driver.get(self.login_url)

        user_email = "brak@gmail.com"
        user_pass = "qwert1234"
        user_login = "Przemek Brak"
        xpath = '//*[@id="_desktop_user_info"]//span'

        functional_helpers.login_funk(driver, user_email, user_pass)
        self.assert_element_text(driver, xpath, user_login)

    def test_name_price_of_tshirt(self):
        driver = self.driver
        driver.get(self.sample_produkt_url)
        xpath = '//*[@id="main"]//*[@itemprop="price"]'
        xpaths = '//*[@id="main"]/div[1]/div[2]/h1'
        expected_text = "HUMMINGBIRD PRINTED T-SHIRT"
        expected_texts = "PLN23.52"

        self.assert_element_text(driver, xpaths, expected_text)

        self.assert_element_text(driver, xpath, expected_texts)

    def test_login_incorrect_mail(self):
        user_login = "test@test.com"
        user_pass = "qwert123"
        xpath = '//*[@class="alert alert-danger"]'
        expected_text = "Authentication failed."
        driver = self.driver
        driver.get(self.base_url)
        click_button_login = driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]//span')
        click_button_login.click()

        functional_helpers.login_funk(driver, user_login, user_pass)
        self.assert_element_text(driver, xpath, expected_text)


