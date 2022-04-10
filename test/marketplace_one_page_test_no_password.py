from test.base_test import BaseTest


class SaveSearchDataTest(BaseTest):

    def test_group(self):
        marketplace_page = self.getMarketplace()
        marketplace_page.input_search(description="1")
        marketplace_page.move_down_page(description="2", numbers=int(2))
        list_id = marketplace_page.get_list_id_href_ads(description="3")
        list_id_data = marketplace_page.get_list_data_id_list()
        marketplace_page.save_error(text= "find ads = "+str(len(list_id)))
        number_new_ads = 0
        for ad_id in list_id:
            boolean = True
            for i in list_id_data:
                if ad_id in i:
                    boolean = False                  
            if boolean:
                number_new_ads +=1
                marketplace_page.open_one_ads(ad_id=ad_id, description="4")
                try:
                    marketplace_page.expand_text(description="5")
                except:
                    pass
                marketplace_page.get_data_page(description="6")
                list_button_foto = marketplace_page.get_list_button_foto()
                marketplace_page.save_error(text="\t" + str(ad_id) + "\t" + str(len(list_button_foto)))        
                for i in range(0, len(list_button_foto)):
                    try:
                        list_button_foto[i].click()
                        marketplace_page.save_image()
                    except:
                        marketplace_page.save_error(text="\t" +"error_write " +str(ad_id) + "\t" +str(i)+ "\t" + str(len(list_button_foto)))
        marketplace_page.save_error(text= "add ads = " + str(number_new_ads))
