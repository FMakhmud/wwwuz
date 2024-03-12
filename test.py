import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        self.browser.get("https://toshkent-parfum.uz/")
        # self.browser.save_screenshot('screenshot1.png')

        self.assertIn("Toshkent parfum", self.browser.title)
        login_button = self.browser.find_element(By.CSS_SELECTOR, 'button.button')
        self.assertIsNotNone(login_button)

        input_phone_number = self.browser.find_element(By.ID, 'phone_number')
        input_password = self.browser.find_element(By.ID, 'password')


        input_phone_number.send_keys('990000000')
        input_password.send_keys('password')
        button_login = self.browser.find_element(By.CLASS_NAME,
                                                 'button rounded-lg !py-2 !px-4 md:py-2.5 md:px-3 flex-center cursor-pointer transition-300 relative button-primary w-full')
        button_login.click()
        time.sleep(4)


if __name__ == "__main__":
    unittest.main()
