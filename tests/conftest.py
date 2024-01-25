from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
import pytest

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        service_obj = ChromeService("C:\\Users\\HP\\Documents\\chromedriver.exe")
        try:
            driver = webdriver.Chrome(service=service_obj)
        except Exception as e:
            print(f"Error during WebDriver setup: {e}")
            raise  # Re-raise the exception to propagate the error
    elif browser_name == "firefox":
        service_obj = Service("C:\\Users\\HP\\Documents\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()


    request.cls.driver = driver

    yield

    driver.close()





