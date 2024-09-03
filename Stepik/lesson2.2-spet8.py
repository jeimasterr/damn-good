from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)



try:
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']") # Поиск 1 поля
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']") # Поиск 2 поля
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']") # Поиск 3 поля
    input3.send_keys("Smolensk") 

    element_import = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    element_import.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, "btn")  # Находим кнопку Submit
    submit_button.click()





finally:
    time.sleep(4)
    browser.quit()
    print("Done")