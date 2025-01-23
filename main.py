
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

from selenium import webdriver

from OfficePage import OfficePage
from MainPage import MainPage
from LoginPage import LoginPage
from UploadingReportPage import UploadingReportPage

from PageException import PageException

SUBJECT_NAME = "Языки информационного обмена"

if __name__ == '__main__':
    driver = webdriver.Firefox()

    try:
        load_dotenv()
        username=os.getenv('USERNAME')
        password=os.getenv('PASSWORD')
        url=os.getenv('URL')
        hw_file_path=os.getenv('HW_FILE_PATH')

        if not os.path.exists(hw_file_path):
            raise FileNotFoundError(f"Файл не найден: {hw_file_path}")

        print("Открываем страницу:", url)
        driver.get(url)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Страница загружена успешно!")

        print("Переходим на страницу входа")
        main_page = MainPage(driver)
        main_page.go_to_login_page()

        print("Авторизуемся")
        login_page = LoginPage(driver)
        login_page.login(username=username, password=password)

        print("Переходим на страницу загрузки отчетов")
        office_page = OfficePage(driver)
        office_page.go_to_uploading_report_page()

        print("Загружаем файл")
        uploading_report_page = UploadingReportPage(driver)
        uploading_report_page.upload_hw(subject_name=SUBJECT_NAME, file_path=hw_file_path)

    except PageException as e:
        print("Something went wrong with pages")
        print("Error details:", str(e))
        traceback.print_exc()
    except Exception as e:
        print("An unexpected error occurred:")
        print("Error details:", str(e))
        traceback.print_exc()
    finally:
        print("Программа завершена.")
