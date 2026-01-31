# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"


# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()


def test_registration1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Заполняем обязательные поля
        browser.find_element(
            By.CSS_SELECTOR, ".first_block .first_class input"
        ).send_keys("Иван")
        browser.find_element(
            By.CSS_SELECTOR, ".first_block .second_class input"
        ).send_keys("Иванов")
        browser.find_element(
            By.CSS_SELECTOR, ".first_block .third_class input"
        ).send_keys("test@example.com")

        # Отправляем форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!"

    finally:
        browser.quit()
