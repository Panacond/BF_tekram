from test.base_test import BaseTest


class SaveSearchDataTest(BaseTest):

    def test_group(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email(description="1")
        home_page.input_password(description="2")
        home_page.click_button_come_in(description="3")
        # TODO зайти на поиск
        # TODO select geolocation!!!
        URL_MARKETPLACE_SEARCH = "https://www.facebook.com/marketplace/115427551801302/search?query={search}"
        # TODO промотать вниз на каждые 4 объявления на пол экрана
        # TODO получить список
        # TODO бесконечный цикл поиска
        # условие остановки если набралось 10 объявлений с неправильным местоположением
        # нет, увеличить списко на 50 объявлений еще раз выбрать все подходящие
        LIST_AD = "//a[contains(@href,'/marketplace/item/')]"
        # TODO цикл по объявлению
            # TODO получить  href
            # TODO получить ID
            # TODO проверить это обявление в базе данных если нет и он локация соотвествует
                # TODO зайти на элемент
                # TODO через try выбрать следующие элементы:
                    # TODO заголовок
        TITLE = "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 qg6bub1s iv3no6db o0t2es00 f530mmz5 hnhda86s oo9gr5id']"
                    # TODO описание
        DESCRIPTION = "//div[@class='ii04i59q a8nywdso f10w8fjw rz4wbd8a pybr56ya']/div/span"
                    # TODO price
        PRICE = "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em mdeji52x a5q79mjw g1cxx5fr ekzkrbhg oo9gr5id']"
                # TODO geolocation
        GEOLOCATION = "//div[contains(@style,'language=en')]"
                # TODO save_in_data_base one row
                # [href, id, title, price, description, geolocation]
                # TODO сохранить фото цикл
                # TODO  сохранить фото
                # TODO цикл кликнуть на 2(начиная с 0) элемент
        LIST_BUTTON_FOTO = "//img[@class='k4urcfbm bixrwtb6 datstx6m']"
                    # TODO сохрать фото (дата и ID)
        LARGE_FOTO = "//img[@alt='No photo description available.']"
                # TODO вернуться назад
