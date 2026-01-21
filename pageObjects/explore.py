import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ExplorePage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.explore_tab = (By.ID, "6_heade_tab")
        self.products_tab = (By.ID, "Products")
        self.mutual_funds_tab = (By.ID, "0_explore_activeTab")
        self.ipo_tab = (By.ID, "1_explore_activeTab")
        self.global_investing_tab = (By.ID, "2_explore_activeTab")
        self.tax_filling_tab = (By.ID, "3_explore_activeTab")
        self.nps_online_tab = (By.ID, "4_explore_activeTab")
        self.grobox_tab = (By.ID, "5_explore_activeTab")
        self.smallcase_tab = (By.ID, "6_explore_activeTab")
        self.tradebox_tab = (By.ID, "7_explore_activeTab")
        self.instaoptions_tab = (By.ID, "8_explore_activeTab")
        self.more_tab = (By.ID, "More")
        self.form_format_tab = (By.ID, "0_explore_activeTab")
        self.offer_to_tab = (By.ID, "1_explore_activeTab")
        self.offer_for_sale_tab = (By.ID, "2_explore_activeTab")

    def explore_button(self, test_results, expected="pass"):
        elements = [
            ("explore_tab", self.explore_tab),
            ("products_tab", self.products_tab),
            ("mutual_funds_tab", self.mutual_funds_tab),
            ("ipo_tab", self.ipo_tab),
            ("global_investing_tab", self.global_investing_tab),
            ("tax_filling_tab", self.tax_filling_tab),
            ("nps_online_tab", self.nps_online_tab),
            ("grobox_tab", self.grobox_tab),
            ("smallcase_tab", self.smallcase_tab),
            ("tradebox_tab", self.tradebox_tab),
            ("instaoptions_tab", self.instaoptions_tab),
            ("more_tab", self.more_tab),
            ("form_format_tab", self.form_format_tab),
            ("offer_to_tab", self.offer_to_tab),
            ("offer_for_sale_tab", self.offer_for_sale_tab),

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
                "Page": "Explore",
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
