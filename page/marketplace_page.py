from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from page.BasePage import screen
from data.read_data import write_csv
import re

class Marketplace(BasePage):

    GROUP_LIST = "//a[contains(@href,'https://www.facebook.com/groups')]"