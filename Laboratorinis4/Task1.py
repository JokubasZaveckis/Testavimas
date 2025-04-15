from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 1. Laukia kol kaina pasieks 100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Spaudzia book mygtuka
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 3. Issprendzia lygti
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(answer)

    # 4. Spaudzia submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(7)
    browser.quit()
