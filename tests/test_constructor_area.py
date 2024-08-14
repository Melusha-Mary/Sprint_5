import time

from data import Data
from locators import StellarBurgerLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSwitchingConstructorSections:
    def test_switch_to_buns_section(self, driver):
        login_in_account_button = driver.find_element(*StellarBurgerLocators.LOGIN_IN_ACCOUNT_BUTTON)
        login_in_account_button.click()
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.CONSTRUCTOR_BUTTON))

        constructor_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(StellarBurgerLocators.BUN_BUTTON))

        bun_button = driver.find_element(*StellarBurgerLocators.BUN_BUTTON)
        sauce_button = driver.find_element(*StellarBurgerLocators.SAUCE_BUTTON)
        bun_active_button = driver.find_element(*StellarBurgerLocators.BUN_ACTIVE_BUTTON)

        sauce_button.click()
        bun_button.click()

        assert driver.find_element(*StellarBurgerLocators.BUN_ACTIVE_BUTTON)

    def test_switch_to_sauce_section(self, driver):
        login_in_account_button = driver.find_element(*StellarBurgerLocators.LOGIN_IN_ACCOUNT_BUTTON)
        login_in_account_button.click()
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.CONSTRUCTOR_BUTTON))

        constructor_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(
            StellarBurgerLocators.SAUCE_BUTTON))

        sauce_button = driver.find_element(*StellarBurgerLocators.SAUCE_BUTTON)

        sauce_button.click()

        assert driver.find_element(*StellarBurgerLocators.SAUCE_ACTIVE_BUTTON)

    def test_switch_to_fillers_section(self, driver):
        login_in_account_button = driver.find_element(*StellarBurgerLocators.LOGIN_IN_ACCOUNT_BUTTON)
        login_in_account_button.click()
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.CONSTRUCTOR_BUTTON))

        constructor_button = driver.find_element(*StellarBurgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(
            StellarBurgerLocators.SAUCE_BUTTON))

        fillers_button = driver.find_element(*StellarBurgerLocators.FILLINGS_BUTTON)

        fillers_button.click()

        assert driver.find_element(*StellarBurgerLocators.FILLINGS_ACTIVE_BUTTON)
