from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Basket_page(Base):  #корзина

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    basket_word = '//h1[@class="cat_full_name" and text()="Корзина"]' # локатор для проверки что мы на странице корзина
    number_of_positions = '//input[@class="purchased_product"]' # количество позиций
    not_available_word = '//span[normalize-space(text())="(Нет в наличии)"]'# нет в наличии
    remove_product = '//img[@class="remove_product"]' # удалить из корзины
    pickup = '//span[text()="Самовывоз"]' # самовывоз
    pickup_metro_yuzhnoe = '//input[@id="store_yuzhnaya"]' # самовывоз метро южное
    pickup_metro_savelovskoye = '//input[@id="store_savelovskaya"]'# самовывоз метро савеловское
    pickup_metro_entuziastov = '//input[@id="store_shosse_entuziastov"]' # cамовывоз м. Шоссе Энтузиастов
    pickup_mitinsky_radio_market = '//input[@id="store_mitino"]'# cамовывоз из ПВЗ Митинский радиорынок
    by_courier_mkad = '//span[text()="Курьером в пределах МКАД"]'# курьером в пределах МКАД
    payment_cash = '//input[@name="radio_method_pay" and @value="cash"]'# оплата наличными
    cashless_payment = '//input[@name="radio_method_pay" and @value="bank"]' # безналичный расчет
    placing_an_order = '//span[@class="create_order"]'# оформляем заказ

    # Getters

    def get_basket_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_word)))

    def get_number_of_positions(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_of_positions)))

    def get_remove_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_product)))

    def get_not_available_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.not_available_word)))


    def get_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup)))

    def get_pickup_metro_yuzhnoe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_metro_yuzhnoe)))

    def get_pickup_metro_savelovskoye(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_metro_savelovskoye)))

    def get_pickup_metro_entuziastov(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_metro_entuziastov)))

    def get_pickup_mitinsky_radio_market(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_mitinsky_radio_market)))

    def get_by_courier_mkad(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.by_courier_mkad)))

    def get_payment_cash(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_cash)))

    def get_cashless_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cashless_payment)))

    def get_placing_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.placing_an_order)))



    # Actions

    def click_number_of_positions(self):
        self.get_number_of_positions().click()
        print("Click number of positions")

    def click_remove_product(self):
        self.get_remove_product().click()
        print("Click remove product")

    def click_pickup(self):
        self.get_pickup().click()
        print("Click pickup")

    def click_pickup_metro_yuzhnoe(self):
        self.get_pickup_metro_yuzhnoe().click()
        print("Click pickup metro yuzhnoe")

    def click_pickup_metro_savelovskoye(self):
        self.get_pickup_metro_savelovskoye().click()
        print("Click pickup metro savelovskoye")

    def click_pickup_metro_entuziastov(self):
        self.get_pickup_metro_entuziastov().click()
        print("Click pickup metro entuziastov")

    def click_pickup_mitinsky_radio_market(self):
        self.get_pickup_mitinsky_radio_market().click()
        print("Click pickup mitinsky radio market")

    def click_by_courier_mkad(self):
        self.get_by_courier_mkad().click()
        print("Click by courier mkad")

    def click_payment_cash(self):
        self.get_payment_cash().click()
        print("Click payment cash")

    def click_cashless_payment(self):
        self.get_cashless_payment().click()
        print("Click cashless payment")


    def click_placing_an_order(self):
        button = self.get_placing_an_order()
        if button.is_enabled():
            button.click()
            print("Click placing an order")
        else:
            print("Order cannot be placed")


    # Methods


    def product_order_1(self):
        self.get_current_url()
        self.refresh_page()
        self.assert_word(self.get_basket_word(), "Корзина")
        self.get_screenshot()
        self.click_pickup()
        self.click_by_courier_mkad()
        self.get_screenshot()
        self.click_placing_an_order()

    def product_order_2(self):
        self.get_current_url()
        self.refresh_page()
        self.assert_word(self.get_basket_word(), "Корзина")
        self.get_screenshot()
        self.click_remove_product()
        self.click_pickup_mitinsky_radio_market()
        self.click_cashless_payment()
        self.click_placing_an_order()

    def product_order_3(self):
        self.get_current_url()
        self.refresh_page()
        self.assert_word(self.get_basket_word(), "Корзина")
        self.get_screenshot()
        self.click_pickup_metro_entuziastov()
        self.click_cashless_payment()
        self.click_payment_cash()
        self.get_screenshot()
        self.click_placing_an_order()


    def product_order_4(self):
        self.get_current_url()
        self.refresh_page()
        self.assert_word(self.get_basket_word(), "Корзина")
        self.get_screenshot()
        self.click_pickup_metro_entuziastov()
        self.click_pickup_mitinsky_radio_market()
        self.get_screenshot()
        self.click_cashless_payment()
        self.click_payment_cash()
        self.get_screenshot()
        self.click_placing_an_order()
