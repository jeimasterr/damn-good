from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) # Функция подсчета значения y



try:
    x_element = browser.find_element(By.ID, "input_value") # Поиск значения x
    x = x_element.text # Присвоение переменной x значения 
    y = calc(x) # Вызов функции 

    input_x = browser.find_element(By.ID, "answer") # Находим поле для ввода значения y
    input_x.send_keys(y) # Вбиваем значение y в поле

    checkbox = browser.find_element(By.CSS_SELECTOR, "[type=checkbox]") # Находим чек бокс
    checkbox.click()

    radio_button = browser.find_element(By.CSS_SELECTOR, "[for=robotsRule]") # Находим радио баттон с названием Robots rule
    radio_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")    # Находим кнопку подтверждения (Sumbit)
    submit_button.click()



finally:

    time.sleep(3)
    browser.quit()
    print("Done")
