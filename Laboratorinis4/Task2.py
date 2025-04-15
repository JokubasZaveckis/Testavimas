from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_form_and_submit(url):
    browser = webdriver.Chrome()
    browser.get(url)

    try:
        # Uzpildo reikalingus duomenis
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Jokubas")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Zaveckis")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("jokubas@example.com")

        # Spaudzia submit
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(2)

        # Issaugo rezultata
        return browser.find_element(By.TAG_NAME, "h1").text
    finally:
        browser.quit()

# Testas su 1 nuoroda
try:
    result1 = fill_form_and_submit("http://suninjuly.github.io/registration1.html")
    if "Congratulations" in result1:
        print("Pirma nuoroda suveike gerai. (Tiketasi)")
    else:
        print("Pirma nuooda failino. (Nesitiketa)")
except Exception as e:
    print("Exception:", e)

# Testas su 2 nuoroda
try:
    result2 = fill_form_and_submit("http://suninjuly.github.io/registration2.html")
    if "Congratulations" in result2:
        print("Antra nuoroda suveike gerai. (Nesitiketa).")
    else:
        print("Antra nuoroda failino. (Tiketasi).")
except Exception:
    print("Antra nuoroda failino. (Tiketasi).")
