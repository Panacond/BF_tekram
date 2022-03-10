from test.base_test import BaseTest


class FantasticPageTest(BaseTest):

    def test_group(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email(description="1")
        home_page.input_password(description="2")
        home_page.click_button_come_in(description="3")
        # home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        # home_page.click_button_enter_select_account()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_search(text="фантастика", description="4")
        group_page = self.getGroupPage()
        group_page.wait_visibility_of_element(self.DEFAULT_TIMEOUT, group_page.WAIT_ELEMENT)
        group_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        list_group = group_page.get_list_group(description="5")
        set_element = list_group[9]
        group_page.set_id_group(set_element)
        group_page.wait_visibility_of_element(self.DEFAULT_TIMEOUT, group_page.WAIT_ELEMENT)
        group_page.one_group_click(description="6")
        group_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        group_page.click_media(description="7")
        group_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        group_page.move_down_page(description="8", numbers=10)
        list_foto = group_page.get_list_foto(description="9")
        group_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        one_foto = list_foto[33]
        group_page.set_id_foto(one_foto)
        group_page.one_foto_click(description="9")
        group_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        group_page.save_image()
        group_page.save_comment()

