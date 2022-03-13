from test.base_test import BaseTest


class HomePageTest(BaseTest):

    def test_check_in_to_site(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email(description="01-01")
        home_page.input_password(description="01-02")
        home_page.click_button_come_in(description="01-03")
        # if select account
        # home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        # home_page.click_button_enter_select_account()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        assert home_page.some_text(text="s on your mind, Bill?", description="01-04 fin")

