from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from data import read_data
from datetime import datetime
import sys


def screen(func):
    def wrapper(self, **kwargs):
        a = func(self, **kwargs)
        self.make_screenshot(kwargs['description'])
        return a
    return wrapper


class BasePage(object):
    NAME_SYSTEM = "linux" == print(sys.platform)
    PATH_SAVE_SCREENSHOTS = "recourses/screenshot/"
    PATH_SAVE_IMAGE = "recourses/foto/"
    # PATH_SAVE_IMAGE = "recourses/screenshot/"
    PATH_SAVE_DATA = "recourses/"
    data_base = read_data.SearchData(PATH_SAVE_DATA + "data")

    def __init__(self, driver):
        self.driver = driver

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def wait_visibility_of_element(self, second, xpath):
        wait = WebDriverWait(self.driver, second)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    @staticmethod
    def text_time_now():
        now_time = str(datetime.now())
        now_time = now_time.replace(" ", "_")
        now_time = now_time.replace(".", "_")
        now_time = now_time.replace(":", "-")
        return now_time

    def make_screenshot(self, description="_"):
        now_time = self.PATH_SAVE_SCREENSHOTS + self.text_time_now() + "_" + description + '.png'
        self.driver.save_screenshot(now_time)

    @screen
    def refresh(self, **kwargs):
        self.driver.refresh()
