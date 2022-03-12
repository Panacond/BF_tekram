from page.group_page import GroupPage
from selenium.webdriver.common.by import By
from page.BasePage import screen


class OneFotoPage(GroupPage):

    id_foto = None

    @screen
    def one_foto_in_new_tab(self, **kwargs):
        """[description]"""
        # https://www.facebook.com/photo/?fbid=146018534532011&set=g.1769191590003361
        # https://www.facebook.com/photo/?fbid={id_foto}&set=g.{id_group}
        url = GroupPage.URL_ONE_FOTO.format(id_foto=self.id_foto, id_group=self.id_group)
        self.driver.execute_script("window.open('');")
        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[kwargs['index']])
        self.driver.get(url)

    def save_image_folder(self):
        now_time = str(self.text_time_now())
        with open(self.PATH_SAVE_IMAGE + now_time + "_" + self.id_foto + '_img.jpg', 'wb') as file:
            img = self.driver.find_element(By.XPATH, self.SAVE_IMAGE)
            file.write(img.screenshot_as_png)

    def close_current_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def go_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
