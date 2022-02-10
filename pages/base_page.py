from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seleniumpagefactory.Pagefactory import PageFactory


class BasePage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def wait_visibility_of_element(self, second, element):
        wait = WebDriverWait(self.driver, second)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, element)))
