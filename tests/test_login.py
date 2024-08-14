from data import Data
from locators import StellarBurgerLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarBurgerLogin:
    def test_login_by_login_button_on_main(self, driver):
        login_in_account_button = driver.find_element(*StellarBurgerLocators.LOGIN_IN_ACCOUNT_BUTTON)
        login_in_account_button.click()
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PLACING_ORDER_BUTTON))

        placing_order_button = driver.find_element(*StellarBurgerLocators.PLACING_ORDER_BUTTON)
        assert placing_order_button.is_displayed()

    def test_login_from_personal_area(self, driver):
        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()
        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PLACING_ORDER_BUTTON))

        placing_order_button = driver.find_element(*StellarBurgerLocators.PLACING_ORDER_BUTTON)
        assert placing_order_button.is_displayed()

    def test_login_from_registration_area(self, driver):
        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.REGISTRATION_BUTTON))

        registration_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.LOGIN_BUTTON_IN_REGISTRATION_AREA))

        login_button_in_reg_area = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON_IN_REGISTRATION_AREA)
        login_button_in_reg_area.click()

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PLACING_ORDER_BUTTON))

        placing_order_button = driver.find_element(*StellarBurgerLocators.PLACING_ORDER_BUTTON)
        assert placing_order_button.is_displayed()

    def test_login_from_password_recovery_area(self, driver):
        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PASSWORD_RECOVERY_BUTTON))

        password_recovery_button = driver.find_element(*StellarBurgerLocators.PASSWORD_RECOVERY_BUTTON)
        password_recovery_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.LOGIN_BUTTON_IN_REGISTRATION_AREA))

        login_button_in_password_recovery_area = driver.find_element(
            *StellarBurgerLocators.LOGIN_BUTTON_IN_REGISTRATION_AREA)
        login_button_in_password_recovery_area.click()

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(Data.login)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.password)

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PLACING_ORDER_BUTTON))

        placing_order_button = driver.find_element(*StellarBurgerLocators.PLACING_ORDER_BUTTON)
        assert placing_order_button.is_displayed()
