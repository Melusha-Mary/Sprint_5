from data import Data, URL
from locators import StellarBurgerLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestGoToConstructor:
    def test_go_to_constructor_by_button(self, driver):
        login_in_account_button = driver.find_element(*StellarBurgerLocators.LOGIN_IN_ACCOUNT_BUTTON)
        login_in_account_button.click()
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PERSONAL_AREA_BUTTON))

        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_matches(URL.StellarBurger_Personal_Area_URL))

        constructor_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.MAKE_BURGER_HEADER))

        make_burger_header = driver.find_element(*StellarBurgerLocators.MAKE_BURGER_HEADER)

        assert make_burger_header.is_displayed()

    def test_go_to_constructor_by_logo(self, driver):
        login_in_account_button = driver.find_element(*StellarBurgerLocators.LOGIN_IN_ACCOUNT_BUTTON)
        login_in_account_button.click()
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PERSONAL_AREA_BUTTON))

        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_matches(URL.StellarBurger_Personal_Area_URL))

        burger_logo = driver.find_element(*StellarBurgerLocators.STELLAR_BURGERS_LOGO)
        burger_logo.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.MAKE_BURGER_HEADER))

        make_burger_header = driver.find_element(*StellarBurgerLocators.MAKE_BURGER_HEADER)

        assert make_burger_header.is_displayed()
