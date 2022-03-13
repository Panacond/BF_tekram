from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from page.BasePage import screen
from data.read_data import write_csv
import re


class GroupPage(BasePage):
    
    GROUP_LIST = "//a[contains(@href,'https://www.facebook.com/groups')]"
    FIND_LIST = "//i[@data-visualcompletion='css-img']"
    PASSWORD = "//input[@id='m_login_password']"
    BUTTON_COME_IN = "//button[@name='login']"
    BUTTON_ENTER_SELECT_ACCOUNT = "//button[@type='submit']"
    WAIT_ELEMENT = "//span[text()='See all']"
    BUTTON_MEDIA = "//a[contains(@href,'media')]/div/span[text()='Media']"
    BUTTON_FOTO = "//a[@href='/groups/{group_id}/media/photos/']"
    LIST_FOTO = "//a[contains(@href,'/photo/')]"
    # LIST_FOTO = "//div[@class='k4urcfbm l9j0dhe7 datstx6m htq0iepx']"
    SAVE_IMAGE = "//img[@data-visualcompletion='media-vc-image']"
    LIST_COMMENT = "//span[contains(@class,'2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn hrzyx87i jq4qci2q a3bd9o3v b1v8xokw oo9gr5id')]"
    URL_ONE_GROUP = "https://www.facebook.com/groups/{group}/"
    URL_ONE_FOTO = "https://www.facebook.com/photo/?fbid={id_foto}&set=g.{id_group}"
    id_group = None
    page_url = None
    id_foto = None
    comment_list = ["text"]

    @screen
    def get_list_group(self, **kwargs):
        return self.driver.find_elements(By.XPATH, self.GROUP_LIST)

    def click_group(self, **kwargs):
        """[element, description]"""
        kwargs['element'].click()
        self.make_screenshot(kwargs['description'])

    @screen
    def one_foto_click(self, **kwargs):
        """[description]"""
        # https://www.facebook.com/photo/?fbid=146018534532011&set=g.1769191590003361
        # https://www.facebook.com/photo/?fbid={id_foto}&set=g.{id_group}
        url = self.URL_ONE_FOTO.format(id_foto=self.id_foto, id_group=self.id_group)
        self.driver.get(url)

    @screen
    def one_group_click(self, **kwargs):
        url = self.URL_ONE_GROUP.format(group=self.id_group)
        self.driver.get(url)

    @screen
    def click_media(self, **kwargs):
        self.driver.find_element(By.XPATH, self.BUTTON_MEDIA).click()

    def view_button_foto(self):
        self.driver.find_element(By.XPATH, self.BUTTON_FOTO.format(group_id=self.id_group))

    @screen
    def click_foto(self, **kwargs):
        self.driver.find_element(By.XPATH, self.BUTTON_FOTO.format(group_id=self.id_group)).click()

    @screen
    def get_list_foto(self, **kwargs):
        return self.driver.find_elements(By.XPATH, self.LIST_FOTO)

    @screen
    def get_list_id_foto(self, **kwargs):
        list_foto = self.driver.find_elements(By.XPATH, self.LIST_FOTO)
        list_id = []
        for element in list_foto:
            href = element.get_attribute('href')
            list_id.append(str(re.search(r"(fbid=)(.*)(&set)", href).group(2)))
        return list_id

    def move_down_page(self, **kwargs):
        if kwargs["numbers"]:
            scroll = int(kwargs["numbers"]) + 1
        else:
            scroll = 2
        self.driver.execute_script("window.scrollTo(0,"+str(scroll) + ")")
        for i in range(1, scroll):
            self.driver.execute_script('window.scrollTo(0,{0})'.format(str(540 * i)))
            self.make_screenshot(kwargs['description'] + str(i))

    def set_id_group(self, element):
        href = element.get_attribute('href')
        self.id_group = str(re.search(r"(groups/)([^/]*)", href).group(2))
        one_row = [
            ["href_group", href],
            ["id_group", self.id_group]
        ]
        write_csv(self.PATH_SAVE_DATA + "data", one_row)

    def set_id_foto(self, element):
        href = element.get_attribute('href')
        self.id_foto = str(re.search(r"(fbid=)(.*)(&set)", href).group(2))
        one_row = [
            ["href_foto", href],
            ["id_foto", self.id_foto]
        ]
        write_csv(self.PATH_SAVE_DATA + "data", one_row)

    def string_url(self):
        self.page_url = self.driver.current_url
        return self.page_url

    def save_image(self):
        now_time = str(self.text_time_now())
        with open(self.PATH_SAVE_SCREENSHOTS + now_time + '_img.jpg', 'wb') as file:
            img = self.driver.find_element(By.XPATH, self.SAVE_IMAGE)
            file.write(img.screenshot_as_png)

    def save_comment(self):
        comment_list = self.driver.find_elements(By.XPATH, GroupPage.LIST_COMMENT)
        text_list_comment = ['comment']
        for item in comment_list:
            text = item.text
            text = text.replace('"', "'")
            text = text.replace('\n', "\t")
            text_list_comment.append(text)
        one_row = [text_list_comment]
        write_csv(self.PATH_SAVE_DATA + "data", one_row)

    def save_data(self):
        data_list = [
            ["ID_group", self.id_group],
            ["URL", self.page_url],
            self.comment_list
        ]
        write_csv(self.PATH_SAVE_DATA + "data", data_list)

    @screen
    def open_foto(self, **kwargs):
        """[description]"""
        url = GroupPage.URL_ONE_FOTO.format(id_foto=self.id_foto, id_group=self.id_group)
        self.driver.get(url)

    @screen
    def open_foto_by_id(self, **kwargs):
        """[description]"""
        url = GroupPage.URL_ONE_FOTO.format(id_foto=kwargs['id_foto'], id_group=self.id_group)
        self.driver.get(url)

    def save_image_folder(self, id_foto):
        now_time = str(self.text_time_now())
        with open(self.PATH_SAVE_IMAGE + now_time + "_" + id_foto + '_img.jpg', 'wb') as file:
            img = self.driver.find_element(By.XPATH, self.SAVE_IMAGE)
            file.write(img.screenshot_as_png)

