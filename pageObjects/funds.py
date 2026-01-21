import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class FundsPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.funds_tab = (By.ID, '5_heade_tab')
        self.add_withdrawal_fund = (By.XPATH, "//button[normalize-space(text())='Add/Withdraw']")
        self.funds_available = (
            By.XPATH, "//button[@type='button' and @class='cursor-pointer']/img[@alt='downExpandArrow']/parent::button")
        self.collateral_available = (
            By.XPATH, "//button[@type='button' and @class='cursor-pointer'][.//img[@alt='downExpandArrow']]")

    def funds_button(self, test_results, expected="pass"):
        elements = [
            ("funds_tab", self.funds_tab),
            ("add_withdrawal_fund", self.add_withdrawal_fund),
            ("funds_available", self.funds_available),
            ("collateral_available", self.collateral_available),
        ]
        for name, locator in elements:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)
                ).click()
                time.sleep(5)
                status = "pass"
                actual_error = ""

            except Exception as e:
                status = "fail"
                actual_error = "XPath not found or invalid xpath"

            test_results.append({
                "Page": "Funds",
                "Testing_Area": name,
                "expected": expected,
                "actual": "clicked successfully" if status == "pass" else actual_error,
                "status": status
            })



    def get_login_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None
