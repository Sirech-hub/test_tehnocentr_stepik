import datetime
import os


class Base():

    def __init__(self, driver):
        self.driver = driver

    """ Method get current url """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    """ Method assert word """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """ Method screenshot """

    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot_" + now_date + '.png'
        screenshot_path = os.path.join("C:\\Users\\Larkov\\PycharmProjects\\final_project\\screen", name_screenshot)
        self.driver.save_screenshot(screenshot_path)

    """ Method assert url """
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")


    """ Method scrollpage """
    def scroll_page(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    """ Сlear input field """

    def clear_input_field(self, element):
        element.clear()

    """ Enter number """

    def enter_number_of_positions(self, field, number_of_positions):  # вводит нужное количество позиций в поле по ключу
        field.clear()
        field.send_keys(str())

    """ Refresh page """
    def refresh_page(self):
        self.driver.refresh()
        print("Page has been refreshed.")

