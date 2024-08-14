from selenium.webdriver.common.by import By


class StellarBurgerLocators:
    LOGIN_INPUT_FIELD = (By.XPATH, "//input[@name='name']")  # Поле логина в окне входа
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Пароль']")  # Поле пароля в окне входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "войти" в окне входа
    LOGIN_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    PLACING_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка оформления заказа
    PERSONAL_AREA_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка перехода в Личный кабинет
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Кнопка Регистрации в окне Личный кабинет
    LOGIN_BUTTON_IN_REGISTRATION_AREA = (By.XPATH, "//a[text()='Войти']")  # Кнопка "Войти" в окне регистрации
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # Кнопка "Восстановить пароль"
    NAME_REGISTRATION_INPUT_FIELD = (By.XPATH, "//fieldset[1]//input")  # Поле ИМЯ в окне регистрации
    EMAIL_REGISTRATION_INPUT_FIELD = (By.XPATH, "//fieldset[2]//input")  # Поле EMAIL в окне регистрации
    PASSWORD_REGISTRATION_INPUT_FIELD = (By.XPATH, "//fieldset[3]//input")  # Поле PASSWORD в окне регистрации
    REGISTRATION_BUTTON_IN_REGISTRATION_AREA = (
        By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка зарегистрироваться
    REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об ошибке при регистрации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка перехода в конструктор в шапке
    MAKE_BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип бургерной в шапке
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выйти в Личном кабинете
    BUN_BUTTON = (By.XPATH, "//span[text()='Булки']")  # Кнопка перехода в раздел "Булки"
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']")  # Кнопка перехода в раздел "Соусы"
    FILLINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']")  # Кнопка перехода в раздел "Начинки"
    BUN_ACTIVE_BUTTON = (
        By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, '2BEP')]")  # Активная кнопка раздела "Булки"
    SAUCE_ACTIVE_BUTTON = (
        By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, '2BEP')]")  # Активная кнопка раздела "Соусы"
    FILLINGS_ACTIVE_BUTTON = (
        By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, '2BEP')]")  # Активная кнопка раздела "Начинки"
    BUN_HEADER = (By.XPATH, "//h2[text()='Булки']")  # Заголовок раздела "Булки"
    SAUCE_HEADER = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок раздела "Соусы"
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок раздела "Начинки"
    CONSTRUCTOR_ACTIVE_SECTION_BUTTON_ATT = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
    # Значение аттрибута class для активной кнопки переключения режимов
    HEADER_LOCATION = {'x': 332, 'y': 244}  # Координаты для поиска заголовков
    ERROR_MESSAGE_TEXT = 'Некорректный пароль'  # Текст ошибки для неверного пароля
