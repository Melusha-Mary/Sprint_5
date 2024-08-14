from data import Data
from locators import StellarBurgerLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from generators import Generators


class TestStellarBurgerRegistration:
    def test_successful_registration(self, driver):
        generated_name = Generators.generate_name()
        generated_email = Generators.generate_email()
        generated_correct_password = Generators.generate_correct_password()

        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.REGISTRATION_BUTTON))

        registration_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.NAME_REGISTRATION_INPUT_FIELD))

        name_input_field = driver.find_element(*StellarBurgerLocators.NAME_REGISTRATION_INPUT_FIELD)
        name_input_field.send_keys(generated_name)

        email_input_field = driver.find_element(*StellarBurgerLocators.EMAIL_REGISTRATION_INPUT_FIELD)
        email_input_field.send_keys(generated_email)

        password_input_field = driver.find_element(*StellarBurgerLocators.PASSWORD_REGISTRATION_INPUT_FIELD)
        password_input_field.send_keys(generated_correct_password)

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.REGISTRATION_BUTTON_IN_REGISTRATION_AREA))

        register_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_BUTTON_IN_REGISTRATION_AREA)
        register_button.click()

        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.LOGIN_INPUT_FIELD))

        login_input = driver.find_element(*StellarBurgerLocators.LOGIN_INPUT_FIELD)
        login_input.send_keys(generated_email)

        password_input = driver.find_element(*StellarBurgerLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(generated_correct_password)

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.LOGIN_BUTTON))

        login_button = driver.find_element(*StellarBurgerLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.PLACING_ORDER_BUTTON))

        placing_order_button = driver.find_element(*StellarBurgerLocators.PLACING_ORDER_BUTTON)
        assert placing_order_button.is_displayed()

    def test_unsuccessful_registration_incorrect_password(self, driver):
        generated_name = Generators.generate_name()
        generated_email = Generators.generate_email()
        generated_wrong_password = Generators.generate_wrong_password()

        personal_area_button = driver.find_element(*StellarBurgerLocators.PERSONAL_AREA_BUTTON)
        personal_area_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.REGISTRATION_BUTTON))

        registration_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(StellarBurgerLocators.NAME_REGISTRATION_INPUT_FIELD))

        name_input_field = driver.find_element(*StellarBurgerLocators.NAME_REGISTRATION_INPUT_FIELD)
        name_input_field.send_keys(generated_name)

        email_input_field = driver.find_element(*StellarBurgerLocators.EMAIL_REGISTRATION_INPUT_FIELD)
        email_input_field.send_keys(generated_email)

        password_input_field = driver.find_element(*StellarBurgerLocators.PASSWORD_REGISTRATION_INPUT_FIELD)
        password_input_field.send_keys(generated_wrong_password)

        register_button = driver.find_element(*StellarBurgerLocators.REGISTRATION_BUTTON_IN_REGISTRATION_AREA)
        register_button.click()

        assert driver.find_element(
            *StellarBurgerLocators.REGISTRATION_ERROR_MESSAGE).text == StellarBurgerLocators.ERROR_MESSAGE_TEXT
