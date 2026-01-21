import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils


class otpPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.otp_inputs_locator = (By.CSS_SELECTOR, "#otp_input > div > input")
        self.verify_forgot_otp = (By.ID, "totp_btn")
        self.login_error_locator = (By.CSS_SELECTOR, ".login_error_height")
        self.risk_disclosure_button = (By.XPATH, "//button[@type='button' and text()='Acknowledge']")

    def enter_input(self, otp: str) -> bool:
        try:
            # 👉 1. Click Get Mobile OTP
            btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Get Mobile OTP"))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)

            # Wait for all OTP input fields
            otp_inputs = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located(self.otp_inputs_locator)
            )

            print(f"✅ OTP Inputs found: {len(otp_inputs)}")

            if len(otp_inputs) != len(otp):
                print("❌ Error: OTP input count does not match OTP length.")
                return False

            # Enter each OTP digit
            for i, digit in enumerate(otp):
                otp_inputs[i].click()
                otp_inputs[i].clear()
                otp_inputs[i].send_keys(digit)
                time.sleep(0.2)  # simulate user typing
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.verify_forgot_otp)
            ).click()

            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(self.risk_disclosure_button)
            ).click()

            return True

        except Exception as e:
            print(f"❌ Exception while entering OTP: {e}")
            return False

    # def verifyForgototp(self) -> bool:
    #     try:
    #         # Wait until the button is clickable and then click
    #
    #         print("✅ Verify OTP button clicked.")
    #         return True
    #     except Exception as e:
    #         print(f"❌ Failed to click Verify OTP button: {e}")
    #         return False

    def get_login_error(self):
        try:
            # Wait briefly for any login error to appear
            error_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.login_error_locator)
            )
            error_text = error_element.text.strip()
            print(f"⚠️ Login error found: {error_text}")
            return error_text
        except:
            return None
