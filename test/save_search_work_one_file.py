from test.base_test import BaseTest


class SaveSearchDataTest(BaseTest):

    def test_group(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email(description="1")
        home_page.input_password(description="2")
        home_page.click_button_come_in(description="3")
        home_page.input_search(text="group paint", description="4")
        group_page = self.getGroupPage()
        list_group = group_page.get_list_group(description="5")
        set_element = list_group[1]
        group_page.set_id_group(set_element)
        group_page.one_group_click(description="6")
        group_page.click_media(description="7")
        group_page.move_down_page(description="8", numbers=2)
        list_id_foto = group_page.get_list_id_foto(description="9")
        for one_id_foto in list_id_foto:
            group_page.open_foto_by_id(id_foto=one_id_foto, description="10")
            group_page.save_image_folder(id_foto=one_id_foto)
            group_page.save_comment()
