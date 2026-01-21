import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WatchList(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_scrip_input = (By.ID, 'watch_search_inp')

        self.predefined_tab = (By.ID, "mw_Predefined List_tab")
        self.my_stock_button = (By.XPATH, "//a[span[text()='MY STOCKS']]")
        self.nifty_stock = (By.XPATH, "//a[span[text()='NIFTY 5000']]")
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
        self.edit_button = (By.ID, "Edit_btn")
        self.cursor_button = (By.CSS_SELECTOR,
                              "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3) > svg:nth-child(1)")
        self.cursor_button_2 = (By.CSS_SELECTOR,
                                "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > a:nth-child(3) > svg:nth-child(1)")
        self.cursor_button_3 = (By.CSS_SELECTOR,
                                "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > a:nth-child(3) > svg:nth-child(1)")
        self.cursor_button_4 = (By.CSS_SELECTOR,
                                "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > a:nth-child(3) > svg:nth-child(1)")
        self.cursor_button_5 = (By.CSS_SELECTOR,
                                "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > a:nth-child(3) > svg:nth-child(1)")

        self.close_button = (By.CSS_SELECTOR,
                             "button[class='size-8 bg-[#0d45930f] text-center primaryColor mr-2 cursor-pointer flex justify-center items-center rounded']")
        self.add_scrips = (By.CSS_SELECTOR,
                           "button[class='size-8 bg-[#44b748] border-[#44b748] flex justify-center items-center rounded text-center text-white cursor-pointer']")

        self.watchlist_input_field = (By.ID, "renameInp_0")
        self.watchlist_input_field_2 = (By.ID, "renameInp_1")
        # self.watchlist_input_field_3 = (By.ID, "renameInp_2")
        # self.watchlist_input_field_4 = (By.ID, "renameInp_3")
        # self.watchlist_input_field_5 = (By.ID, "renameInp_4")

    def watchlist_setting(self, test_results, expected="pass"):

        elements = [
            ("setting_icon", self.setting_icon),
            ("sort_scrips", self.sort_scrips),
            ("percentage", self.percentage),
            ("ltp_button", self.ltp_button),
            ("preference_button", self.preference_button),
            ("small_button", self.small_button),
            ("medium_button", self.medium_button),
            ("large_button", self.large_button),
            ("xtra_large_button", self.xtra_large_button),
            ("basic_radio_box", self.basic_radio_box),
            ("depth_radio_box", self.depth_radio_box),
            ("all_radio_box", self.all_radio_box),
            ("top_radio_box", self.top_radio_box),
            ("bottom_radio_box", self.bottom_radio_box),
            ("depth_radio_box", self.basic_radio_box),
            ("all_radio_box", self.all_radio_box),
            ("edit_button", self.edit_button),

            # add more buttons if needed
        ]

        for name, locator in elements:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)
                ).click()
                time.sleep(2)
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

        new_names = ["Watchlist1", "Watchlist2", "Watchlist3", "Watchlist4", "Watchlist5"]

        status = "pass"
        actual_error = ""

        try:
            for idx, new_name in enumerate(new_names):
                # Always fetch edit button fresh (avoid stale element issue)
                edit_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f"(//a//*[name()='svg'][contains(@class,'cursor-pointer')])[{idx + 1}]")
                    )
                )
                edit_button.click()

                # Wait for the input field to appear for this row
                input_field = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, f"//input[contains(@id,'renameInp_')]")
                    )
                )

                # Clear and type new name
                input_field.clear()
                input_field.send_keys(new_name)

                # Click the ✔ save button for this row
                save_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[@type='submit' and contains(@class,'bg-[#44b748]')]")
                    )
                )
                save_button.click()

                # Small wait for DOM to stabilize before next loop
                time.sleep(1)
            actual_error = "Renamed all watchlists successfully"

        except Exception as e:
            status = "fail"
            actual_error = str(e)

        test_results.append({
            "watchlist_bottom_tab": "watchlist rename",
            "expected": "All 5 lists renamed",
            "actual": actual_error,
            "status": status
        })
        # Step 2: Rename Watchlists

    def get_login_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None
