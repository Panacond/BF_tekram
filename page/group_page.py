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
    # LIST_FOTO = "//a[contains(@href,'/photo/')]"
    LIST_FOTO = "//div[@class='k4urcfbm l9j0dhe7 datstx6m htq0iepx']"
    SAVE_IMAGE = "//img[@data-visualcompletion='media-vc-image']"
    LIST_COMMENT = "//span[contains(@class,'2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn hrzyx87i jq4qci2q a3bd9o3v b1v8xokw oo9gr5id')]"

    id_group = None
    page_url = None
    comment_list = ["text"]

    @screen
    def get_list_group(self, **kwargs):
        return self.driver.find_elements(By.XPATH, self.GROUP_LIST)

    def click_group(self, element, **kwargs):
        element.click()
        self.make_screenshot(kwargs['description'])

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
        # print(href)
        self.id_group = str(re.search(r"(groups\/)([^\/]*)", href).group(2))
        # print(self.id_group)

    def string_url(self):
        self.page_url = self.driver.current_url
        return self.page_url

    def save_image(self):
        now_time = str(self.text_time_now())
        with open(self.PATH_SAVE_IMAGE + now_time + '_img.jpg', 'wb') as file:
            img = self.driver.find_element(By.XPATH, self.SAVE_IMAGE)
            file.write(img.screenshot_as_png)

    def save_comment(self):
        comment_list = self.driver.find_elements(By.XPATH, self.LIST_COMMENT)
        for item in comment_list:
            text = item.text
            text = text.replace('"', "'")
            text = text.replace('\n', "\t")
            self.comment_list.append(text)

    def save_data(self):
        data_list = [
            ["ID_group", self.id_group],
            ["URL", self.page_url],
            self.comment_list
        ]
        write_csv(self.PATH_SAVE_DATA + "data", data_list)


