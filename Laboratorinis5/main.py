import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def create_driver():
    options = Options()
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")

    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")
    service = Service(executable_path=chromedriver_path)

    return webdriver.Chrome(service=service, options=options)

# Funkcijos lygio fixture: nauja narsykle kiekvienam testui
@pytest.fixture(scope="function")
def browser():
    print("\n[Paruosimas] Paleidziama narsykle testui")
    driver = create_driver()
    yield driver
    print("\n[Uzbaigimas] Narsykle uzdaroma po testo")
    driver.quit()

# Klases lygio fixture: viena narsykle visai testu klasei
@pytest.fixture(scope="class")
def browser_class():
    print("\n[Paruosimas] Paleidziama narsykle testu klasei")
    driver = create_driver()
    yield driver
    print("\n[Uzbaigimas] Narsykle uzdaroma po testu klases")
    driver.quit()

# Modulio lygio fixture: viena narsykle visam failui
@pytest.fixture(scope="module")
def browser_module():
    print("\n[Paruosimas] Paleidziama narsykle moduliui")
    driver = create_driver()
    yield driver
    print("\n[Uzbaigimas] Narsykle uzdaroma po modulio")
    driver.quit()

# Sesijos lygio fixture: vykdoma viena karta visai testu sesijai
@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    print("\n[Sesijos pradzia] Pradedama testavimo sesija")
    yield
    print("\n[Sesijos pabaiga] Testavimo sesija baigta")

class TestRegistrationFunctionScope:
    """Testai su funkcijos lygio narsykles fixture."""

    def test_registration1(self, browser):
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Test")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Test")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("Test")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "h1"),
                "Congratulations! You have successfully registered!"
            )
        )
        assert browser.find_element(By.TAG_NAME, "h1").text == "Congratulations! You have successfully registered!"

    @pytest.mark.xfail(reason="registration2 truksta privalomo lauko", strict=False)
    def test_registration2(self, browser):
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Test")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Test")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("Test")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "h1"),
                "Congratulations! You have successfully registered!"
            )
        )
        assert browser.find_element(By.TAG_NAME, "h1").text == "Congratulations! You have successfully registered!"

class TestRegistrationClassScope:
    """Testai su klases lygio narsykles fixture."""

    @pytest.fixture(autouse=True)
    def _browser(self, browser_class):
        self.browser = browser_class

    def test_reg1_class(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Test")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Test")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("Test")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "h1"),
                "Congratulations! You have successfully registered!"
            )
        )
        assert self.browser.find_element(By.TAG_NAME, "h1").text == "Congratulations! You have successfully registered!"

    @pytest.mark.xfail(reason="registration2 truksta privalomo lauko", strict=False)
    def test_reg2_class(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Test")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Test")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("Test")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "h1"),
                "Congratulations! You have successfully registered!"
            )
        )
        assert self.browser.find_element(By.TAG_NAME, "h1").text == "Congratulations! You have successfully registered!"
