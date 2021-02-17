from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x, y):

  return str(int(x) + int(y))


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    x = x_element.text
    y = y_element.text
    result = calc(x, y)
    print(result)
    
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(result)


    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(3)

finally:
    time.sleep(10)
    browser.quit()


