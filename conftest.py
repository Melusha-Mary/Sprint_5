import pytest
from data import URL
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(URL.StellarBurger_Main_URL)
    chrome_driver.set_window_size(1366, 768)
    yield chrome_driver
    chrome_driver.quit()
