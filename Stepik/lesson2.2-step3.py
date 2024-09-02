from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html" # Ссылка на сайт

browser = webdriver.Chrome() # Инициализация браузера
browser.get(link) # Открытие ссылки


try:
    num1 = int(browser.find_element(By.ID, "num1").text) # Находим первое число и забираем текст из него -> Переводим в инт
    num2 = int(browser.find_element(By.ID, "num2").text) # Находим второе число и забираем текст из него -> Переводим в инт

    answer = num1 + num2 # Складываем данные числа для ответа


    select_list = Select(browser.find_element(By.TAG_NAME, "select")) # Сначала ищем Элемент (Выпадающий список) и затем выбираем его
    select_list.select_by_value(str(answer)) # Выбираем элемент выпадающего списка по значению 48

    submit_button = browser.find_element(By.CLASS_NAME, "btn").click() # Находим кнопку Submit и кликаем по ней


finally:
    time.sleep(3)
    browser.quit() # Закрываем браузер
    print("Done")