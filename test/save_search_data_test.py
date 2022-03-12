from test.base_test import BaseTest


class SaveSearchDataTest(BaseTest):

    def test_group(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email(description="1")
        home_page.input_password(description="2")
        home_page.click_button_come_in(description="3")
        home_page.input_search(text="group yacht", description="4")
        group_page = self.getGroupPage()
        list_group = group_page.get_list_group(description="5")
        set_element = list_group[3]
        group_page.set_id_group(set_element)
        group_page.one_group_click(description="6")
        group_page.click_media(description="7")
        group_page.move_down_page(description="8", numbers=2)
        list_foto = group_page.get_list_foto(description="9")
        one_foto_page = self.getOneFotoPage()
        one_foto_page.id_group = group_page.id_group
        one_foto_page.set_id_foto(list_foto[0])
        one_foto_page.one_foto_in_new_tab(description="10", index=1)
        one_foto_page.go_first_tab()
        for one_foto in list_foto:
            one_foto_page.set_id_foto(one_foto)
            one_foto_page.one_foto_in_new_tab(description="11", index=2)
            one_foto_page.save_image_folder()
            one_foto_page.save_comment()
            one_foto_page.close_current_tab()
