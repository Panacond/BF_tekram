import unittest
from selenium import webdriver
from page.HomePage import HomePage
from page.group_page import GroupPage
from page.one_foto_page import OneFotoPage
from page.marketplace_page import Marketplace
import os
from screen_recorder_sdk import screen_recorder
from data.read_data import write_csv


class BaseTest(unittest.TestCase):
    
    DEFAULT_TIMEOUT = 50

    def setUp(self):

        path = HomePage.PATH_SAVE_SCREENSHOTS
        # makes list file and delete
        for file in os.listdir(path + '.'):
            print(file)
            os.remove(path + file)

        if HomePage.NAME_SYSTEM:
            params = screen_recorder.RecorderParams()
            # initialize the screen recorder
            screen_recorder.init_resources(params)
            screen_recorder.start_video_recording(HomePage.text_time_now() + 'movie.mp4', 30, 8000000, True)

        self.driver = webdriver.Chrome()
        self.driver.get("https://facebook.com/")
        self.driver.maximize_window()
        one_row = [["time", HomePage.text_time_now()]]
        write_csv(HomePage.PATH_SAVE_DATA + "data", one_row)

    def tearDown(self):
        self.driver.close()
        if HomePage.NAME_SYSTEM:
            screen_recorder.stop_video_recording()

    def getHomePage(self):
        return HomePage(self.driver)

    def getGroupPage(self):
        return GroupPage(self.driver)

    def getOneFotoPage(self):
        return OneFotoPage(self.driver)

    def getMarketplace(self):
        return Marketplace(self.driver)

