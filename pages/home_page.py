from pages.base_page import BasePage
from data import read_data


class HomePage(BasePage):
    locators = {
        "email": ('XPATH', "//input[@id='m_login_email']"),
        "password": ('XPATH', "//input[@id='m_login_password']"),
        "button_come_in": ('XPATH', "//button[@name='login']"),
        "button_enter_select_account": ('XPATH', "//button[@type='submit']"),
    }

    def input_email(self):
        # email = read_data.search_element('email')
        self.email.set_text("")

    def input_password(self):
        # password = read_data.search_element('password')
        self.password.set_text("")

    def click_button_come_in(self):
        self.button_come_in.click_button()

    def click_button_enter_select_account(self):
        self.button_enter_select_account.click_button()

    def click_button_xiaomi(self):
        # self.button_xiaomi.click_button()
        self.driver.find_element_by_xpath(self.locators.get("button_xiaomi")[1]).click()

if __name__ == '__main__':
    data = read_data.read_file('recourses/data')
    print(data)