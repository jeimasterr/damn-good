import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
try:
    # Запуск браузера
    driver = webdriver.Chrome()
    time.sleep(3)

    # Заходим на сайт
    driver.get("https://rms2.develop.efood.dev/")
    time.sleep(2)


    # Находим "Крестик"
    button_close = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(13) > div > div > section > svg")
    button_close.click() #Нажимаем на крестик
    time.sleep(3)

    # Находим кнопку принять куки
    cookie_close = driver.find_element(By.CSS_SELECTOR, "#__next > div._1H4WTf._2YuC59 > button")
    cookie_close.click() #Кликаем на кнопку "Принять"
    time.sleep(1)

    # Находим кнопку "В корзину"
    add_item = driver.find_element(By.CSS_SELECTOR, "#__next > div.gJ_uxB > section > main > section:nth-child(1) > div._1HjFB1 > article:nth-child(1) > div.mChQYM > div.GWFgdO > div")
    add_item.click() #Клик на кнопку "В корзину"
    time.sleep(5)
finally:
    driver.quit() #Закрываем браузер