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
        list_id = marketplace_page.get_list_id_href_ads(description="5")
        list_id_data = marketplace_page.get_list_data_id_list()
        for ad_id in list_id:
            boolean = True
            for i in list_id_data:
                if ad_id in i:
                    boolean = False
            if boolean:
                marketplace_page.open_one_ads(ad_id=ad_id, description="8")
                marketplace_page.get_data_page(description="9")
                list_button_foto = marketplace_page.get_list_button_foto()
                for i in range(2, len(list_button_foto)):
                    list_button_foto[i].click()
                    marketplace_page.save_image()
