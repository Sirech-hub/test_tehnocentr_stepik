from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.catalog_page import Catalog_page
from pages.login_page import Login_page


def test_buy_product_1(set_up):
    options = webdriver.ChromeOptions()
    driver_path = r'C:\Users\Larkov\PycharmProjects\resource\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    print("Start")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.select_product_random()

def test_buy_product_2(set_up):
    options = webdriver.ChromeOptions()
    driver_path = r'C:\Users\Larkov\PycharmProjects\resource\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    print("Start")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.select_product_2()

def test_buy_product_3(set_up):
    options = webdriver.ChromeOptions()
    driver_path = r'C:\Users\Larkov\PycharmProjects\resource\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    print("Start")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.select_product_1()










