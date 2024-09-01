from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) # Функция подсчета значения y



try:
    x_element = browser.find_element(By.ID, "treasure") # Поиск значения x
    x = x_element.get_attribute("valuex") # Присвоение переменной x значения 
    assert x is not None, "Нет значения X"
    y = calc(x) # Вызов функции 

    input_x = browser.find_element(By.ID, "answer") # Находим поле для ввода значения y
    input_x.send_keys(y) # Вбиваем значение y в поле

    checkbox = browser.find_element(By.CSS_SELECTOR, "[type=checkbox]") # Находим чек бокс
    checkbox.click()

    radio_button = browser.find_element(By.ID, "robotsRule") # Находим радио баттон с названием Robots rule
    radio_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")    # Находим кнопку подтверждения (Sumbit)
    submit_button.click()



finally:

    time.sleep(3)
    browser.quit()
    print("Done")
