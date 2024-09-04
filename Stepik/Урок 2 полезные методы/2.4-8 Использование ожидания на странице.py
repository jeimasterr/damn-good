from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
import time

browser = webdriver.Chrome()

def calc(x):
    return log(abs(12*sin(x)))

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 13 секунд, когда значение text будет 100
price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), text_="$100")
    )

message = browser.find_element(By.ID, "book") # Ищем кнопку Book
message.click()
browser.execute_script("window.scrollBy(0, 100);") # Скролл в самый низ

x_element = int(browser.find_element(By.ID, "input_value").text) # Поиск значения x и преобразуем в инт

input_value = browser.find_element(By.ID, "answer") # Ищем поле для ввода значения
input_value.send_keys(calc(x_element))

Submit = browser.find_element(By.ID, "solve") # Ищем кнопку Submit
Submit.click()

time.sleep(4)
browser.quit()
print("Done")