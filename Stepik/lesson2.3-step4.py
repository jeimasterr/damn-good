from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return log(abs(12*sin(x)))


try:

    submit_button = browser.find_element(By.CLASS_NAME, "btn")  # Находим кнопку Submit
    submit_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    x_element = int(browser.find_element(By.ID, "input_value").text)
    x = calc(x_element)

    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(x)

    Submit = browser.find_element(By.CLASS_NAME, "btn")
    Submit.click()





finally:
    time.sleep(4)
    browser.quit()
    print("Done")