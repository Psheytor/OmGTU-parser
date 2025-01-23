from selenium.webdriver.common.by import By

from BasePage import BasePage

class MainPage(BasePage):
    PROFILE_BUTTON_LOCATOR = (By.XPATH,"//a[@class='horizontal-menu__link'][@href='https://omgtu.ru/ecab/']")

    def go_to_login_page(self):
        self.click_element(self.PROFILE_BUTTON_LOCATOR)