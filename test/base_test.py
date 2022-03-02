import unittest
from selenium import webdriver
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):

    DEFAULT_TIMEOUT = 100

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://m.facebook.com/")
        # self.driver.get("https://m.facebook.com/marketplace/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def getHomePage(self):
        return HomePage(self.driver)

