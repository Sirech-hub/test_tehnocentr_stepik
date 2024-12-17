from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import random

class Catalog_page(Base): # каталог товаров и методы работы с ним

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators описание каталога товаров и ключей

    key_1 = random.randint(1, 33) # рандомный ключ для локатора категории товара
    key_2 = random.randint(1, 5)  # рандомный ключ для локатора  продукта

    search_by_name = '//input[@placeholder="Поиск по каталогу товаров"]' # поиск товара по конкретному названию в поле ввода (самый удобный способ поиска при реальной работе с сайтом)
    product_category_1 = '//a[@class="cat_item" and text()[normalize-space(.)="Оперативная память"]]' # категория товара Оперативная память
    product_category_2 = '//a[@class="cat_item" and text()[normalize-space(.)="Расходные материалы"]]' # категория товара Расходные материалы
    product_category_3 = '//a[@class="cat_item" and text()[normalize-space(.)="Шлейфы матриц"]]' # категория товара Шлейфы матриц
    product_category_random = f'(//a[@class="cat_item"])[{key_1}]' # иногда падают не успевают прогрузиться
    product_1_word = '//h1[@class="cat_full_name" and text()="Оперативная память"]' # для проверки 1 категории
    switch_to_table = '//a[normalize-space(text())="показать таблицей"]' # переключаем на таблицу всех товаров
    switch_to_classic = '//a[normalize-space(text())="классический вид"]' # переключаем на классический вид
    add_to_cart_by_locator = f'(//img[@class="product_add_cart_ico"])[{key_2}]' # добавляем рандомный товар в корзину по локатору элемента
    add_to_cart = '//div[@class="button_add_to_cart"]'# добавить конкретный товар в корзину
    continue_shopping = '//div[normalize-space(text())="Продолжить покупки"]'   # всплывающее окно продолжить покупки
    place_an_order = '//div[normalize-space(text())="Оформить заказ"]' # всплывающее окно оформить заказ сайт нас сразу переключает в корзину

    # Getters

    def get_search_by_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_by_name)))

    def get_product_category_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_category_1)))

    def get_product_category_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_category_2)))

    def get_product_category_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_category_3)))

    def get_product_category_random(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.product_category_random)))

    def get_product_1_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_word)))

    def get_switch_to_table(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.switch_to_table)))

    def get_switch_to_classic(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.switch_to_classic)))

    def get_add_to_cart_by_locator(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_by_locator)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_continue_shopping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping)))

    def get_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.place_an_order)))


    # Actions
    def input_search_by_name(self, name_product):
        self.get_search_by_name().send_keys(name_product)
        self.get_search_by_name().send_keys(Keys.ENTER)
        print("Input: search by name and press Enter")


    def click_product_category_1(self):
        self.get_product_category_1().click()
        print("Click product category ОЗУ")

    def click_product_category_2(self):
        self.get_product_category_1().click()
        print("Click product category Расходные материалы")

    def click_product_category_3(self):
        self.get_product_category_1().click()
        print("Click product category Шлейфы матриц")

    def click_product_category_random(self):
        self.get_product_category_random().click()
        print("Click product category Рандомная категория")

    def click_switch_to_table(self):
        self.get_switch_to_table().click()
        print("Click switch to table")

    def click_switch_to_classic(self):
        self.get_switch_to_classic().click()
        print("Click switch to classic")

    def click_add_to_cart_by_locator(self): # кнопки не всегда активны тк мб нет в наличии
        try:
            self.get_add_to_cart_by_locator().click()
            print("Click add to cart by locator")
        except Exception as e:
            print(f"Failed to click 'add to cart' button: {e}")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Click switch to classic")


    def click_continue_shopping_try(self): #  работаю не очень стабильно поэтому есть и такое решение
        try:
            # Ожидаем появления alert
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Переключаемся на alert и принимаем его
            alert = self.driver.switch_to.alert
            alert.dismiss()
            print("Alert accepted")
        except Exception as e:
            print(f"Error accepting alert: {e}")

            try:
                self.get_continue_shopping().click()
                print("Click continue shopping")
            except Exception as click_error:
                print(f"Error clicking continue shopping: {click_error}")

    def click_place_an_order_try(self):
        try:
            # Ожидаем появления alert
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Переключаемся на alert и принимаем его
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted")
        except Exception as e:
            print(f"Error accepting alert: {e}")

            try:
                self.get_place_an_order().click()
                print("Click place_an_order")
            except Exception as click_error:
                print(f"Error clicking place_an_order: {click_error}")

    def click_continue_shopping(self):
        self.get_continue_shopping().click()
        print("Click continue shopping")

    def click_place_an_order(self):  # тут по сути  мы сразу переходим в корзину
        self.get_place_an_order().click()
        print("Click place an order")

    # Methods

    def select_product_1(self):
        self.get_current_url()
        self.click_product_category_2()
        self.get_screenshot()
        self.assert_word(self.get_product_1_word(), "Оперативная память")
        self.click_switch_to_table()
        self.get_screenshot()
        self.click_add_to_cart_by_locator()
        self.click_place_an_order()


    def select_product_2(self):
        self.get_current_url()
        self.click_product_category_2()
        self.get_screenshot()
        self.click_switch_to_table()
        self.click_add_to_cart_by_locator()
        self.get_screenshot()
        self.click_place_an_order()

    def select_product_random(self):
        self.get_current_url()
        self.click_product_category_random()
        self.click_switch_to_table()
        self.click_add_to_cart_by_locator()
        self.scroll_page(500)
        self.get_screenshot()
        self.click_continue_shopping()
        self.input_search_by_name("Разъем питания для Lenovo B450") # поиск по имени которое точно есть в БД
        self.click_add_to_cart()
        self.get_screenshot()
        self.click_place_an_order()

