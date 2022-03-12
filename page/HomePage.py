from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from page.BasePage import screen


class HomePage(BasePage):
    EMAIL ="//input[@name='email']"
    PASSWORD = "//input[@name='pass']"
    BUTTON_COME_IN ="//button[@name='login']"
    BUTTON_ENTER_SELECT_ACCOUNT = "//button[@type='submit']"
    # SEARCH = "//input[@type='search']"
    SEARCH ="https://www.facebook.com/search/top?q={search}"
    SEARCH_CLICK = "//span[text()='Search for ']"
    SOME_TEXT = "//span[contains(text(),'{text}')]"

    @screen
    def input_email(self, **kwargs):
        email = self.data_base.search_element('email')
        self.driver.find_element(By.XPATH, self.EMAIL).send_keys(email)

    @screen
    def input_password(self, **kwargs):
        password = self.data_base.search_element('password')
        self.driver.find_element(By.XPATH, self.PASSWORD).send_keys(password)

    @screen
    def click_button_come_in(self, **kwargs):
        self.driver.find_element(By.XPATH, self.BUTTON_COME_IN).click()

    @screen
    def click_button_enter_select_account(self, **kwargs):
        self.driver.find_element(By.XPATH, self.BUTTON_ENTER_SELECT_ACCOUNT).click()

    @screen
    def input_search(self, **kwargs):
        """text, description"""
        # https://www.facebook.com/search/top?q={search}
        url = self.SEARCH.format(search=kwargs['text'])
        self.driver.get(url)

    @screen
    def some_text(self, text, **kwargs):
        if self.driver.find_element(By.XPATH, self.SOME_TEXT.format(text=text)):
            return True
        else:
            return False


