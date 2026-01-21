import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class predefinedWatchList(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_scrip_input = (By.ID, 'watch_search_inp')
        self.predefined_tab = (By.ID, "mw_Predefined List_tab")
        self.my_stock_button = (By.XPATH, "//a[span[text()='MY STOCKS']]")
        self.nifty_stock = (By.XPATH, "//a[span[text()='NIFTY 50']]")
        self.setting_icon = (By.XPATH, '//button[.//div[@id="mw_footer_right"]]')
        self.sort_scrips = (By.ID, "A-Z_btn")
        self.percentage = (By.ID, "(%)_btn")
        self.ltp_button = (By.ID, "LTP_btn")
        self.exec_button = (By.ID, "Exc_btn")
        self.bse_button = (By.ID, "//button[text()='BSE']")
        self.nse_button = (By.ID, "//button[normalize-space(text())='NSE']")
        self.preference_button = (By.ID, "Preference_btn")
        self.small_button = (By.ID, "S_btn")
        self.medium_button = (By.ID, "M_btn")
        self.large_button = (By.ID, "L_btn")
        self.xtra_large_button = (By.ID, "XL_btn")
        self.basic_radio_box = (By.ID, "basic")
        self.basic_radio_box = (By.ID, "basic")
        self.depth_radio_box = (By.ID, "depth")
        self.all_radio_box = (By.ID, "all")
        self.top_radio_box = (By.ID, "top")
        self.bottom_radio_box = (By.ID, "bottom")

    def predefined_watchlist_tab(self, test_results, expected="pass"):
        elements = [
            ("predefined_tab", self.predefined_tab),
            ("my_stock_button", self.my_stock_button),
            ("nifty_button", self.nifty_stock),
            ("setting_icon", self.setting_icon),
            ("sort_scrips", self.sort_scrips),
            ("percentage", self.percentage),
            ("ltp_button", self.ltp_button),
            ("exec_button", self.exec_button),
            ("preference_button", self.preference_button),
            ("small_button", self.small_button),
            ("medium_button", self.medium_button),
            ("large_button", self.large_button),
            ("xtra_large_button", self.xtra_large_button),
            ("basic_radio_box", self.basic_radio_box),
            ("depth_radio_box", self.depth_radio_box),
            ("depth_radio_box", self.all_radio_box),

            # add more buttons if needed
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
                "watchlist_bottom_tab": name,
                "expected": expected,
                "actual": "clicked successfully" if status == "pass" else actual_error,
                "status": status
            })

            time.sleep(2)

    def get_login_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None

    # def predefined_watchlist_tab(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.predefined_tab)
    #     ).click()
    #     time.sleep(5)
    #
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.my_stock_button)
    #     ).click()
    #     time.sleep(5)

    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.setting_icon)
    # ).click()
    # time.sleep(5)
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.sort_scrips)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.percentage)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.ltp_button)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.exec_button)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.preference_button)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.small_button)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.medium_button)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.large_button)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.xtra_large_button)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.basic_radio_box)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.depth_radio_box)
    # ).click()
    #
    # time.sleep(5)
    #
    # WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable(self.all_radio_box)
    # ).click()
    #
    # time.sleep(5)