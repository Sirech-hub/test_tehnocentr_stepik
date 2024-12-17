from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page


def test_login(set_up):
    options = webdriver.ChromeOptions()
    driver_path = r'C:\Users\Larkov\PycharmProjects\resource\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    print("Start")

    login = Login_page(driver)
    login.authorization()











