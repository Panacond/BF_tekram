from test.base_test import BaseTest


class HomePageTest(BaseTest):

    def test_check_in_to_site(self):
        home_page = self.getHomePage()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        home_page.input_email(description="01-01")
        home_page.input_password(description="01-02")
        home_page.click_button_come_in(description="01-03")
        # if select account
        # home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        # home_page.click_button_enter_select_account()
        home_page.implicitly_wait(self.DEFAULT_TIMEOUT)
        assert home_page.some_text(text="s on your mind, Bill?", description="01-04 fin")


# class TestTitle(BaseTest):
#     def testTitle(self):
#         home_page = self.getHomePage()
#         text = home_page.getTitle()
#         HOME_PAGE_TITLE = "AVIC™ - удобный интернет-магазин бытовой техники и электроники в Украине. | Avic";
#         assert text == HOME_PAGE_TITLE

# class SmartphonePageTest(BaseTest):
#     def test_AddToCart(self):
#         home_page = self.getHomePage()
#         home_page.clickButtonCatalog()
#         home_page.clickButtonPhonesAndAccessories()
#         home_page.implicitly_wait(30)
#         phones_accessories_page = self.getPhonesAndAccessoriesPage()
#         phones_accessories_page.clickButtonSmartphones()
#         phones_accessories_page.implicitly_wait(30)
#         smartphone_page = self.getSmartphonePage()
#         smartphone_page.clickFindModel()
#         smartphone_page.waitVisibilityOfElement(30, smartphone_page.ADD_TO_CART)
#         smartphone_page.clickButtonCheckout()
#         assert True == smartphone_page.trueFindXiaomiPocoX3Pro8256GB()