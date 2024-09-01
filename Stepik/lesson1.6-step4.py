import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text") # Открываем сайт

# Находим ссылку по её тексту
link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()
time.sleep(1)


try:

    input1 = browser.find_element(By.TAG_NAME, "input") #Поиск по тегу
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name") # поиск по значению атрибута name
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city") # Поиск по значению класса
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country") # Поиск по айди
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn") # Поиск по селектору
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()