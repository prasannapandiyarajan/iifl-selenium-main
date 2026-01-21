import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OrderBook(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.order_tab = (By.ID, '2_heade_tab')
        self.all_tabs = (By.ID, "//nav[@id='tab_navbar']//a[contains(., 'All')]")

    def order_button(self, test_results, expected="pass"):
        elements = [
            ("order_tab", self.order_tab),
            ("all_tabs", self.all_tabs)
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
                "Page": "OrderBook",
                "Testing_Area": name,
                "expected": expected,
                "actual": "clicked successfully" if status == "pass" else actual_error,
                "status": status
            })

    def order_list(self, test_results, expected="pass"):
        driver = self.driver
        wait = WebDriverWait(driver, 12)
        actions = ActionChains(driver)
        action_log = []

        rows = driver.find_elements(By.XPATH, "//tbody/tr")
        #
        for i, row in enumerate(rows):
            try:
                # re-fetch rows fresh each time (avoid stale element reference)
                rows = driver.find_elements(By.XPATH, "//tbody/tr")
                row = rows[i]

                # click row (optional if required)
                driver.execute_script("arguments[0].scrollIntoView(true);", row)
                row.click()

                # find dot (...) button inside that row
                more_btn = row.find_element(By.XPATH, ".//button[contains(@id,'opt_btn')]")
                driver.execute_script("arguments[0].click();", more_btn)

                # wait and click Info in the dropdown
                info_option = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@role='menu']//div[normalize-space()='Info']"))
                )
                info_option.click()
                time.sleep(2)

                # information_tab = WebDriverWait(driver, 5).until(
                #     EC.element_to_be_clickable((By.XPATH, "// button[span[normalize - space() = 'Information']]"))
                # )
                # information_tab.click()

                history_tab = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='flex max-w-[250px] border-b border-secondary']//button[span[normalize-space()='History']]"))
                )
                history_tab.click()

                cancel_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@class='cancel_btn']"))
                )
                cancel_button.click()


                try:
                    order_close_button = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.XPATH,
                                                    "//button[@type='button' and contains(@class,'grey_btn') and normalize-space(text())='Cancel']"))
                    )
                    order_close_button.click()
                    print("Order window closed.")
                except TimeoutException:
                    # No order window opened, continue
                    print("No order window appeared.")

                # if a popup opens, close it here before next loop
                time.sleep(4)
            except Exception as e:
                print(e)

        for i in range(min(5, len(rows))):  # first 5 rows only
            rows = driver.find_elements(By.XPATH, "//tbody/tr")
            row = rows[i]

            driver.execute_script("arguments[0].scrollIntoView(true);", row)
            row.click()
            try:
                clone_btn = row.find_element(By.XPATH, ".//button[contains(text(),'Clone')]")
                driver.execute_script("arguments[0].click();", clone_btn)
                print(f"✅ Clone clicked for row {i + 1}")
                buy_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[@type='submit' and contains(@class,'green_btn')]//span[normalize-space(text())='Buy']"))
                )
                buy_button.click()
            except Exception as e:
                print(f"No Clone button found in row {i + 1}: {e}")

            time.sleep(1)

    def get_login_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None
