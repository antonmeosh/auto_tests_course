import unittest
from selenium import webdriver


class TestEx16(unittest.TestCase):

    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input")
        input3.send_keys("i.petrov@example.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()


    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input")
        input3.send_keys("i.petrov@example.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()



if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
