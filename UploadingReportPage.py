from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage import BasePage


class UploadingReportPage(BasePage):
    ADD_BUTTON_LOCATOR = (By.XPATH, "//div[span[.='+'] and span[.=' добавить']]")
    INPUT_NAME_LOCATOR = (By.XPATH, "//input[@class='abitinptext']")
    UPLOAD_FILE_LOCATOR = (By.XPATH, "//input[@class='otherf']")
    EXIT_LOCATOR = (By.XPATH, "//div[contains(@onclick, 'getvkrpage') and contains(text(), 'закрыть')]")
    CHOOSE_SUBJECT_LOCATOR = (By.XPATH, "//i[contains(text(), 'выберите...')]")
    UPLOAD_SUCCESS_LOCATOR = (By.XPATH, "//div[contains(text(), 'Загрузка завершена')]")

    def upload_hw(self, file_path, subject_name):
        self.click_element(self.ADD_BUTTON_LOCATOR)

        self.click_element(self.CHOOSE_SUBJECT_LOCATOR)
        subject_locator = (By.XPATH, f"//div[@class='discline' and contains(text(), '{subject_name}')]")
        self.click_element(subject_locator)

        self.send_keys_to_element(self.INPUT_NAME_LOCATOR, subject_name)
        self.send_keys_to_element(self.UPLOAD_FILE_LOCATOR, file_path)

        try:
            WebDriverWait(self.driver, 300).until(
                EC.presence_of_element_located(self.UPLOAD_SUCCESS_LOCATOR)
            )
            print("Загрузка файла завершена успешно!")
        except Exception as e:
            print("Ошибка при загрузке файла:", str(e))