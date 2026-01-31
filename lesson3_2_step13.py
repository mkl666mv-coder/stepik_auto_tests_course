import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        # Заполняем обязательные поля
        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .first_class input"
        ).send_keys("Иван")
        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .second_class input"
        ).send_keys("Иванов")
        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .third_class input"
        ).send_keys("test@example.com")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text
        )

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Заполняем обязательные поля (в registration2 разметка немного отличается)
        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .first_class input"
        ).send_keys("Иван")
        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .second_class input"
        ).send_keys("Иванов")
        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .third_class input"
        ).send_keys("test@example.com")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text
        )


if __name__ == "__main__":
    unittest.main()
