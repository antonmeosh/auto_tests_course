from selenium import webdriver
import time
import math


def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input_res = browser.find_element_by_id('answer')
    input_res.send_keys(y)
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()
    robotRule = browser.find_element_by_css_selector("[value='robots']")
    robotRule.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(3)

finally:
    time.sleep(10)
    browser.quit()
