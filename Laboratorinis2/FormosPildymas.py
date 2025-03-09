from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Svetaines nuoroda
link = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"

# Atidaryti chrome fullscreen
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Uzkrauti chromedriver
service = Service("./chromedriver.exe")

# Nustatyti kelia failo ikelimui
file_to_upload = os.path.abspath("testfile.txt")

browser = None

try:
    browser = webdriver.Chrome(service=service, options=chrome_options)
    
    # Atidaryti nuoroda
    browser.get(link)

    # Palaukti kol uzsikraus
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    
    # Supildyti duomenis
    browser.find_element(By.NAME, "username").send_keys("Jokubas")
    browser.find_element(By.NAME, "password").send_keys("Slaptazodis123")
    browser.find_element(By.NAME, "comments").send_keys("Komentaras.")

    # Ikelti faila
    if os.path.isfile(file_to_upload):
        browser.find_element(By.NAME, "filename").send_keys(file_to_upload)

    # Pasirinkti visus checkboxus
    browser.find_element(By.XPATH, "//input[@type='checkbox' and @value='cb1']").click()
    browser.find_element(By.XPATH, "//input[@type='checkbox' and @value='cb2']").click()
    browser.find_element(By.XPATH, "//input[@type='checkbox' and @value='cb3']").click()

    # Pasirinkti mygtuka
    browser.find_element(By.XPATH, "//input[@type='radio' and @value='rd2']").click()

    # Multi pasirinkimas
    multi_select = Select(browser.find_element(By.NAME, "multipleselect[]"))
    multi_select.select_by_visible_text("Selection Item 1")
    multi_select.select_by_visible_text("Selection Item 3")

    # Dropdowno 3 pasirinkimas
    dropdown = Select(browser.find_element(By.NAME, "dropdown"))
    dropdown.select_by_visible_text("Drop Down Item 3")

    # Submit mygtukas
    browser.find_element(By.XPATH, "//input[@type='submit' and @value='submit']").click()

except Exception as e:
    print("Error:", e)

finally:
    time.sleep(5)
    if browser:
        browser.quit()
