from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/explicit_wait2.html")

house_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))


book_button = browser.find_element_by_id('book')
book_button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
input_res = browser.find_element_by_id('answer')
input_res.send_keys(y)

button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

