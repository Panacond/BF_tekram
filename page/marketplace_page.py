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
    TITLE = "div.dati1w0a.qt6c0cv9.hv4rvrfc.discj3wi > span"
    DESCRIPTION = "//div[@class='ii04i59q a8nywdso f10w8fjw rz4wbd8a pybr56ya']/div/span"
    PRICE = "div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div.dati1w0a.qt6c0cv9.hv4rvrfc.discj3wi > div.aov4n071.j83agx80 > div > span"
    GEOLOCATION = "//div[contains(@style,'language=')]"
    LIST_BUTTON_FOTO = "div.giggcyz0.du4w35lb > div > div > div > div > img"
    LARGE_FOTO = "div.bp9cbjyn.j83agx80.buofh1pr.taijpn5t.ni8dbmo4.stjgntxs.k4urcfbm.du4w35lb > span > div > img"
    EXPAND_TEXT = "span[class*='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua jq4qci2q a3bd9o3v lrazzd5p']"

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
            item_href = element.get_attribute('href')
            list_href.append(item_href)
            list_id.append(str(re.search(r"item\/(\d*)", item_href).group(1)))
        self.list_href = list_href
        self.list_id = list_href
        return list_id

    def get_href_id_one_ads(self, element):
        self.href = element.get_attribute('href')
        self.id_item = str(re.search(r"item\/(\d*)", self.href).group(1))
        # write_csv(self.PATH_SAVE_DATA + "data", one_row)

    def get_list_data_id_list(self):
        data = SearchData(self.PATH_DATA_MARKETPLACE)
        return data.list_element_by_before_name("id")

    def get_list_button_foto(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.LIST_BUTTON_FOTO)

    def save_error(self, text, name_file = "image_error.txt"):
        with open(name_file, "a", encoding='utf-8') as f:
            f.write(text + "\n")

    def save_image(self):
        now_time = str(self.text_time_now())
        try:
            with open(self.PATH_SAVE_IMAGE + now_time + '_' + self.id_item + '_img.jpg', 'wb') as file:
                img = self.driver.find_element(By.CSS_SELECTOR, self.LARGE_FOTO)
                file.write(img.screenshot_as_png)
        except:
            self.save_error(text = self.id_item + now_time)

    @screen
    def one_item_in_new_tab(self, **kwargs):
        """[description]"""
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[kwargs['index']])
        self.driver.get('https://www.facebook.com' + self.href )

    @screen
    def open_one_ads(self, **kwargs):
        """[description]"""
        for href in self.list_href:
            if kwargs['ad_id'] in href:
                self.driver.get(href)
                self.href = href
                self.id_item = kwargs['ad_id']
                return True
        # self.driver.get('https://www.facebook.com' + href)

    @screen
    def expand_text(self, **kwargs):
        """[description]"""
        self.driver.find_element(By.CSS_SELECTOR, self.EXPAND_TEXT).click()

    @screen
    def go_first_tab(self, **kwargs):
        """[description]"""
        self.driver.switch_to.window(self.driver.window_handles[0])

    @screen
    def get_data_page(self, **kwargs):
        self.now_time = str(self.text_time_now())
        try:
            title = self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
        except:
            title = "-"
        try:
            price = self.driver.find_element(By.CSS_SELECTOR, self.PRICE).text
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
        self.one_row = [["time", self.now_time,
                            "id", self.id_item,
                            "href", self.href,
                            "title", title,
                            "price", price,
                            "description", description,
                            "geolocation", geolocation_x, geolocation_y ]]
        write_csv(self.PATH_SAVE_DATA + "data_marketplace", self.one_row)
