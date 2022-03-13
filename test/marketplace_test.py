from test.base_test import BaseTest


class SaveSearchDataTest(BaseTest):

    def test_group(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email(description="1")
        home_page.input_password(description="2")
        home_page.click_button_come_in(description="3")
        marketplace_page = self.getMarketplace()
        marketplace_page.input_search(description="4", search='house')
        marketplace_page.move_down_page(description="5", numbers=int(500))
        list_ads = marketplace_page.get_list_ads(description="5")
        marketplace_page.get_href_id_one_ads(list_ads[0])
        marketplace_page.one_item_in_new_tab(description="6", index=1)
        marketplace_page.go_first_tab(description="7")
        for ad in list_ads:
            marketplace_page.get_href_id_one_ads(ad)
            list_id = marketplace_page.get_list_data_id_list()
            boolean = True
            for i in list_id:
                if marketplace_page.id_item in i:
                    boolean = False
            if boolean:
                marketplace_page.one_item_in_new_tab(description="8", index=1)
                marketplace_page.get_data_page(description="9")
                list_button_foto = marketplace_page.get_list_button_foto()
                for i in range(2, len(list_button_foto)):
                    list_button_foto[i].click()
                    marketplace_page.save_image()
                marketplace_page.go_first_tab(description="10")


class ReadWriteTest(BaseTest):
    def test_group(self):
        marketplace_page = self.getMarketplace()
        marketplace_page.get_data_page(description="9")
        list_id = marketplace_page.get_list_data_id_list()
        print(list_id)

