from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
result = calc(x)
print(result)
result_input = browser.find_element_by_id('answer')
result_input.send_keys(result)

robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()


robotRule = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", robotRule)
robotRule.click()


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

