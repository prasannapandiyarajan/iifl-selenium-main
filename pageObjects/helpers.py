import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils


class Helpers(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def _select_tab(self, name, xpath, action_log):
        tab_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", tab_button)
        tab_button.click()
        time.sleep(1)
        action_log.append(f"Clicked tab: {name}")


    def _place_and_modify_order(self, qty, price, new_qty, new_price, action_log):
        qty_field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "qty")))
        qty_field.clear()
        qty_field.send_keys(qty)
        action_log.append(f"Quantity entered: {qty}")

        price_field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "price")))
        price_field.clear()
        price_field.send_keys(price)
        action_log.append(f"Price entered: {price}")

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.buy_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_buy)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_amo)).click()
        time.sleep(3)

        # Open pending order & modify
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dashboard.order_tab)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dashboard.pending_order)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dashboard.orderbook_modify)).click()
        time.sleep(2)

        qty_field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "qty")))
        qty_field.clear()
        qty_field.send_keys(new_qty)
        action_log.append(f"Quantity modified: {new_qty}")

        price_field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "price")))
        price_field.clear()
        price_field.send_keys(new_price)
        action_log.append(f"Price modified: {new_price}")

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.modify_button)).click()


    def _reopen_first_scrip_order_window(self):
        # Navigate back to market watch and click Buy again
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]"))
        )
        scrip = self.driver.find_element(By.XPATH,
                                         "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scrip)
        ActionChains(self.driver).move_to_element(scrip).perform()
        time.sleep(1)
        buy_button = scrip.find_element(By.XPATH, ".//button[normalize-space()='B']")
        buy_button.click()
        time.sleep(6)
