from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    res_x = browser.find_element_by_id('input_value')
    result = math.ln(abs(12*math.sin(int(res_x))))
    input_res = browser.find_element_by_id('answer')
    input_res.send_keys(result)
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()
    robotRule = browser.find_element_by_css_selector("[value='robots']")
    robotRule.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()