from selenium.webdriver.common.by import By
from page.BasePage import screen
from page.group_page import GroupPage
from data.read_data import SearchData
from data.read_data import write_csv
import re


class Marketplace(GroupPage):
    PATH_DATA_MARKETPLACE = "recourses/data_marketplace_save"
    URL_SEARCH = GroupPage.data_base.search_element("link")
    # URL_MARKETPLACE_SEARCH = "https://www.facebook.com/marketplace/115427551801302/search?query={search}"
    LIST_AD_XPATH = "//a[contains(@href,'/marketplace/item/')]"
    # LIST_PLACE_XPATH = "//a[contains(@href,'/marketplace/item/')]/div/div/div/span/div/span/span"
    TITLE = "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 qg6bub1s iv3no6db o0t2es00 f530mmz5 hnhda86s oo9gr5id']"
    DESCRIPTION = "//div[@class='ii04i59q a8nywdso f10w8fjw rz4wbd8a pybr56ya']/div/span"
    PRICE = "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em mdeji52x a5q79mjw g1cxx5fr ekzkrbhg oo9gr5id']"
    GEOLOCATION = "//div[contains(@style,'language=en')]"
    LIST_BUTTON_FOTO = "//img[@class='k4urcfbm bixrwtb6 datstx6m']"
    LARGE_FOTO = "//img[@alt='No photo description available.']"

    one_row = []
    now_time = "-"
    href = '-'
    id_item = '-'
    list_href = []
    list_id = []

    @screen
    def input_search(self, **kwargs):
        """search, description"""
        url = self.URL_SEARCH
        self.driver.get(url)

    @screen
    def get_list_ads(self, **kwargs):
        """description"""
        return self.driver.find_elements(By.XPATH, self.LIST_AD_XPATH)

    @screen
    def get_list_id_href_ads(self, **kwargs):
        """description"""
        list_href = []
        list_id = []
        list_ads = self.driver.find_elements(By.XPATH, self.LIST_AD_XPATH)
        for element in list_ads:
            list_href.append(element.get_attribute('href'))
            list_id.append(str(re.search(r"(groups/)([^/]*)", self.href).group(2)))
        self.list_href = list_href
        self.list_id = list_id
        return list_id

    def get_href_id_one_ads(self, element):
        self.href = element.get_attribute('href')
        self.id_item = str(re.search(r"(groups/)([^/]*)", self.href).group(2))
        # write_csv(self.PATH_SAVE_DATA + "data", one_row)

    def get_list_data_id_list(self):
        data = SearchData(self.PATH_DATA_MARKETPLACE)
        return data.list_element_by_before_name("id")

    def get_list_button_foto(self):
        return self.driver.find_elements(self.LIST_BUTTON_FOTO)

    def save_image(self):
        now_time = str(self.text_time_now())
        with open(self.PATH_SAVE_IMAGE + now_time + '_' + self.id_item + '_img.jpg', 'wb') as file:
            img = self.driver.find_element(By.XPATH, self.LARGE_FOTO)
            file.write(img.screenshot_as_png)

    @screen
    def one_item_in_new_tab(self, **kwargs):
        """[description]"""
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[kwargs['index']])
        self.driver.get('https://www.facebook.com' + self.href)

    @screen
    def open_one_ads(self, **kwargs):
        """[description]"""
        for href in self.href:
            if kwargs['ad_id'] in href:
                return href
        self.driver.get('https://www.facebook.com' + href)

    @screen
    def go_first_tab(self, **kwargs):
        """[description]"""
        self.driver.switch_to.window(self.driver.window_handles[0])

    @screen
    def get_data_page(self, **kwargs):
        self.now_time = str(self.text_time_now())
        try:
            title = self.driver.find_element(By.XPATH, self.TITLE).text
        except:
            title = "-"
        try:
            price = self.driver.find_element(By.XPATH, self.PRICE).text
        except:
            price = "-"
        try:
            description = self.driver.find_element(By.XPATH, self.DESCRIPTION).text
        except:
            description = "-"
        try:
            geolocation = self.driver.find_element(By.XPATH, self.GEOLOCATION)
            geolocation = geolocation.get_attribute('style')
            geolocation_x = str(re.search(r"center=([\d\.]*)%2C([\d\.]*)", geolocation).group(1))
            geolocation_y = str(re.search(r"center=([\d\.]*)%2C([\d\.]*)", geolocation).group(2))
        except:
            geolocation_x = "-"
            geolocation_y = "-"
        self.one_row.append(["time", self.now_time,
                             "href", self.href,
                             "id", self.id_item,
                             "title", title,
                             "price", price,
                             "description", description,
                             "geolocation", geolocation_x, geolocation_y ])
        write_csv(self.PATH_SAVE_DATA + "data_marketplace", self.one_row)
