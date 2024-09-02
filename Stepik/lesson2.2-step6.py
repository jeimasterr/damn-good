from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return log(abs(12*sin(x)))


try:
    x_element = int(browser.find_element(By.ID, "input_value").text) # Ищем значение x и преобразуем в инт
    x = calc(x_element)

    button = browser.find_element(By.CLASS_NAME, "btn") # Поиск кнопки
    browser.execute_script("window.scrollBy(0, 100);") # Скролл до кнопки
    
    input_x = browser.find_element(By.ID, "answer") # Находим поле для ввода значения y
    input_x.send_keys(x) # Вбиваем значение y в поле

    checkbox = browser.find_element(By.CSS_SELECTOR, "[type=checkbox]") # Находим чек бокс
    checkbox.click()

    radio_button = browser.find_element(By.ID, "robotsRule") # Находим радио баттон с названием Robots rule
    radio_button.click()

    button.click()  




finally:
    time.sleep(4)
    browser.quit()
    print("Done")