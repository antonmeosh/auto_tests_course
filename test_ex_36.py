import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestUfos:
    links = [#'https://stepik.org/lesson/236895/step/1',
             #'https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1',
             'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1',
             'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1',
             'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('link', links)
    def test_links(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(10)
        input1 = browser.find_element_by_css_selector('.textarea.string-quiz__textarea.ember-text-area.ember-view')
        answer = str(math.log(int(time.time())))
        input1.send_keys(answer)
        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        time.sleep(3)
        res_text = browser.find_element_by_css_selector(".smart-hints__hint")
        assert res_text.text == 'Correct!', f'{res_text}'
