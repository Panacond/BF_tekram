from test.base_test import BaseTest


class HomePageTest(BaseTest):

    def test_check_in_to_site(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email()
        home_page.input_password()
        home_page.click_button_come_in()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.click_button_enter_select_account()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)


