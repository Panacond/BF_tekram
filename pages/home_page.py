from pages.base_page import BasePage
from data import read_data


class HomePage(BasePage):
    locators = {
        "email": ('XPATH', "//input[@id='m_login_email']"),
        "password": ('XPATH', "//input[@id='m_login_password']"),
        "button_come_in": ('XPATH', "//button[@name='login']"),
        "button_enter_select_account": ('XPATH', "//button[@type='submit']"),
    }

    data_base = read_data.SearchData("recourses/data")

    def input_email(self):
        email = self.data_base.search_element('email')
        self.email.set_text(email)

    def input_password(self):
        password = self.data_base.search_element('password')
        self.password.set_text(password)

    def click_button_come_in(self):
        self.button_come_in.click_button()

    def click_button_enter_select_account(self):
        self.button_enter_select_account.click_button()

    def click_button_xiaomi(self):
        # self.button_xiaomi.click_button()
        self.driver.find_element_by_xpath(self.locators.get("button_xiaomi")[1]).click()


if __name__ == '__main__':
    data = read_data.SearchData("../recourses/data")
    assert data.search_element("test") == "hello_word!", "incorrect file initial data"