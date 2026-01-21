import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class passwordPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.newPassword_input = (By.CSS_SELECTOR, "#newPasswordRef")
        self.confirmPassword_input = (By.CSS_SELECTOR, "#confirmPasswordRef")
        self.set_password_button = (By.ID, "user_btn")
        self.error_message_selector = (By.CSS_SELECTOR, ".text-red-500")  # Replace with actual class if different

    def password_field(self, newpassword, conformpassword):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.newPassword_input)
            )

            self.driver.find_element(*self.newPassword_input).clear()
            self.driver.find_element(*self.newPassword_input).send_keys(newpassword)

            self.driver.find_element(*self.confirmPassword_input).clear()
            self.driver.find_element(*self.confirmPassword_input).send_keys(conformpassword)

            self.driver.find_element(*self.set_password_button).click()

        except Exception as e:
            print("❌ Error while filling password fields:", e)
            raise

    def get_login_error(self):
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.error_message_selector)
            )
            return error_element.text
        except:
            return None