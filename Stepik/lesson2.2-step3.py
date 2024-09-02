from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html" # Ссылка на сайт

browser = webdriver.Chrome() # Инициализация браузера
browser.get(link) # Открытие ссылки


try:
    num1 = int(browser.find_element(By.ID, "num1").text)
    print(num1)
    num2 = int(browser.find_element(By.ID, "num2").text)
    print(num2)
    answer = num1 + num2


    select_list = Select(browser.find_element(By.TAG_NAME, "select")) # Сначала ищем Элемент (Выпадающий список) и затем выбираем его
    select_list.select_by_value(str(answer)) # Выбираем элемент выпадающего списка по значению 48

    submit_button = browser.find_element(By.CLASS_NAME, "btn").click() # Находим кнопку Submit


finally:
    time.sleep(3)
    browser.quit() # Закрываем браузер
    print("Done")