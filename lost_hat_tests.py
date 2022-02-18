import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import functional_helpers


class LostHatFrontPageTests(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + "login"
        self.sample_produkt_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r'C:\SE\chromedriver.exe')

    def tearDown(self):
        self.driver.close()

    def test_list_element(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'
        driver = self.driver
        driver.get(self.base_url)

        find_slider = driver.find_element(By.XPATH, slider_xpath)

        actual_slider_height = find_slider.size["height"]
        actual_slider_width = find_slider.size["width"]
        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                            f'Expected min height in xpath{slider_xpath} on page {driver.current_url} is smaller then we expected')
        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width, f'Expected min widht is 600px')

    def test_slider_contain_exact_number_of_slides(self):
        driver = self.driver
        expected_amound_of_sliders = 3
        table_xpath = '//*[@id="carousel"]/ul/li'

        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, table_xpath)
        actual_number_of_slider = len(slider_elements)
        print(actual_number_of_slider)
        self.assertEqual(actual_number_of_slider, expected_amound_of_sliders,
                         f'Slides number differ for page {self.base_url}')

    def test_slides_required_title_text(self):
        slides_titles_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        driver = self.driver
        driver.get(self.base_url)
        title_elements = driver.find_elements(By.XPATH, slides_titles_xpath)
        expected_text_included_in_slide = "sample"

        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_included_in_slide, title_element_text_lower,
                              f'Expected text i slider {expected_text_included_in_slide} on side {driver.current_url}')

    def test_main_page_eight_element(self):
        expected_status_page = 8
        page_xpath_element = '//*[@class="product-miniature js-product-miniature"]'
        driver = self.driver
        driver.get(self.base_url)
        find_elements_windows = driver.find_elements(By.XPATH, page_xpath_element)
        value_of_element = len(find_elements_windows)
        self.assertEqual(value_of_element, expected_status_page, f'Products number differ for page {self.base_url}')

