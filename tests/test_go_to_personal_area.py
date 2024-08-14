from data import Data, URL
from locators import StellarBurgerLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class TestPersonalAreaStellarBurgers:
    def test_go_to_personal_area_successful(self, driver):
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
            EC.visibility_of_element_located(StellarBurgerLocators.EXIT_BUTTON))

        assert driver.current_url == URL.StellarBurger_Personal_Area_URL
