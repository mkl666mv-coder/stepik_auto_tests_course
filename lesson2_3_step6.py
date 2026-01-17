# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))


# browser = webdriver.Chrome()

# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser.get(link)

#     # Нажимаем на кнопку
#     button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
#     button.click()

#     opened_page = browser.window_handles[1]
#     browser.switch_to.window(opened_page)

#     # Считываем значение x
#     element_value_x = browser.find_element(By.ID, "input_value").text
#     y = calc(int(element_value_x))

#     # Ввести ответ в текстовое поле.
#     field = browser.find_element(By.ID, "answer")
#     field.send_keys(str(y))

#     # Нажать на кнопку Submit.
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()


# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text