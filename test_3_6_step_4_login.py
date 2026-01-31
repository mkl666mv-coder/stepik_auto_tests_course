import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class Test_stepik:

    def test_login(self, browser):
        link = "https://stepik.org/lesson/236895/step/1?auth=login"
        browser.get(link)
        time.sleep(5)

        enter_button = browser.find_element(
            By.CSS_SELECTOR, 'a[href="/lesson/236895/step/1?auth=login"]'
        )
        # enter_button.click()
        time.sleep(2)

        login_input = browser.find_element(By.ID, "id_login_email")
        # login_input.click()
        login_input.send_keys("mkl1985@mail.ru")

        password_input = browser.find_element(By.ID, "id_login_password")
        # password_input.click()
        password_input.send_keys("mklste777")

        enter_button_sign = browser.find_element(
            By.CSS_SELECTOR, "button.sign-form__btn"
        )
        enter_button_sign.click()
        time.sleep(3)
        try:
            element = browser.find_element(By.CSS_SELECTOR, "img.navbar__profile-img")
            assert element.is_displayed(), "Элемент найден, но не виден на странице"
        except NoSuchElementException:
            assert False, "Элемент с ID 'my-element-id' не найден"
