import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.basket_page import Basket_page
from pages.catalog_page import Catalog_page
from pages.login_page import Login_page


#@pytest.mark.run(order=1)
def test_basket_product_1(set_group):
    options = webdriver.ChromeOptions()
    driver_path = r'C:\Users\Larkov\PycharmProjects\resource\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    print("Start")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.select_product_1()

    bp = Basket_page(driver)
    bp.product_order_1()

    time.sleep(10)

#@pytest.mark.run(order=2)
def test_basket_product_2(set_group):
    options = webdriver.ChromeOptions()
    driver_path = r'C:\Users\Larkov\PycharmProjects\resource\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    print("Start")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.select_product_1()

    bp = Basket_page(driver)
    bp.product_order_2()

#@pytest.mark.run(order=3)
def test_basket_product_3(set_group):
    options = webdriver.ChromeOptions()
    driver_path = r'C:\Users\Larkov\PycharmProjects\resource\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    print("Start")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.product_category_random()

    bp = Basket_page(driver)
    bp.product_order_4()






