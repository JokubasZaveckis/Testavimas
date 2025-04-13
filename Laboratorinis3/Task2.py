from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Push button
    browser.find_element(By.TAG_NAME, "button").click()

    # Switch to new opened tab
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Read capture and set answer
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    # Submit
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()
