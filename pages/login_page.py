from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    url = "https://tehnocentr.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_user_page = '//a[@href="https://tehnocentr.ru/login/"]' # переход на страницу логина с главной страницы
    user_mail = '//input[@placeholder="E-mail"]' # вводим почту
    password = '//input[@name="password"]' # вводим пароль
    button_login = '//div[@class="button_add_to_cart login_submit_btn"]'
    personal_account = '//h1[@class="login_h" and text()="Личный кабинет"]'
    return_to_main_page = '//img[@src="/images/log.gif"]' # возврат на гл сттраницу

    # Getters

    def get_login_user_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_user_page)))

    def get_user_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_personal_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_account)))

    def get_return_to_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.return_to_main_page)))

    # Actions

    def click_login_user_page(self): # переходим на страницу логина с главной
        self.get_login_user_page().click()
        print("Click login user page")

    def input_user_mail(self, user_mail): # вводим почту
        self.get_user_mail().send_keys(user_mail)
        print("Input user mail")

    def input_password(self, password): # вводим пароль
        self.get_password().send_keys(password)
        print("Input password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click login button")

    def click_return_to_main_page(self):
        self.get_return_to_main_page().click()
        print("Click return to main page")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_user_page()
        self.input_user_mail("sirech@mail.ru")
        self.input_password("45322") # пароль другой
        self.click_button_login()
        self.assert_word(self.get_personal_account(), "Личный кабинет") # проверяем что вошли в лк
        self.get_screenshot()
        self.click_return_to_main_page() # возвращаемся на главную страницу



