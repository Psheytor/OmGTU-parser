from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PageException import PageException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def wait_for_element(self, locator):
        try:
            print(f"Ожидание элемента: {locator}")
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Элемент не найден: {locator}")
            raise PageException(f"Failed to find element: {locator}") from e

    def click_element(self, locator):
        try:
            self.wait_for_element(locator).click()
            print(f"Клик по элементу: {locator}")

        except Exception as e:
            print(f"Не удалось кликнуть по элементу: {locator}")
            raise PageException(f"Failed to click element: {locator}") from e

    def send_keys_to_element(self, locator, text):
        try:
            print(f"Ввод текста '{text}' в элемент: {locator}")
            self.wait_for_element(locator).send_keys(text)
        except Exception as e:
            print(f"Не удалось ввести текст в элемент: {locator}")
            raise PageException(f"Failed to send keys to element: {locator}") from e