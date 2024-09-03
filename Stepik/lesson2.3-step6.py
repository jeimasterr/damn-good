from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

# Функция для подсчета по формуле
def calc(x):
    return log(abs(12*sin(x)))


try:

    submit_button = browser.find_element(By.CLASS_NAME, "trollface")  # Находим кнопку Submit
    submit_button.click()

    new_window = browser.window_handles[1] # Присваиваем переменной new_window Вторую вкладку
    browser.switch_to.window(new_window) # Переключаемся На вторую вкладку


    x_element = int(browser.find_element(By.ID, "input_value").text) # Находим значение элемента x и преобразовываем в инт
    x = calc(x_element)                                              # Обращаемся к функции calc для подсчета по формуле

    input_value = browser.find_element(By.ID, "answer") # Ищем поле для ввода значения
    input_value.send_keys(x)

    Submit = browser.find_element(By.CLASS_NAME, "btn") # Ищем кнопку Submit
    Submit.click()





finally:
    time.sleep(4)
    browser.quit()
    print("Done")