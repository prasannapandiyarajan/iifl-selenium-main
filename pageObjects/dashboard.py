import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class dashBoardPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_tab = (By.ID, '0_heade_tab')
        self.stock_holding = (By.ID, 'holdinds_widget_header')
        self.home_funds_label = (By.ID, 'home_funds_label')
        self.investment = (By.ID, 'investment')
        self.Current_value = (By.ID, 'Current_value')
        self.profit_loss = (By.ID, 'profit_loss')
        self.todays_pnl = (By.ID, 'todays_pnl')
        self.home_funds_label = (By.ID, 'home_funds_label')
        self.ava_label = (By.ID, 'ava_label')
        self.margin_used_label = (By.ID, 'margin_used_label')
        self.open_bal_label = (By.ID, 'open_bal_label')
        self.payIn_nav = (By.ID, 'payIn_nav')
        self.grobox_iifl = (By.ID, 'smallCases_head')
        self.insta_options = (By.ID, 'smallCases_head')
        self.invest_stock_label = (By.ID, 'invest_stock_label')
        self.equities_ideas = (By.ID, 'Equity Ideas')
        self.equit_tab = (By.XPATH, "//nav[@id='tab_navbar']//a[@id='Equity']")
        self.equities_ideas = (By.XPATH, "//div[@id='Equity Ideas' and contains(@class, 'cursor-pointer')]")
        self.long_term = (By.XPATH, "//button[span[text()='Long Term']]")
        self.short_term = (By.XPATH, "//button[span[text()='Short Term']]")
        self.intraday = (By.XPATH, "//button[span[text()='Intraday']]")
        self.drop_down = (By.XPATH, "//button[.//span[text()='All Calls']]")
        self.all_calls = (By.XPATH, "//ul[@role='listbox']//li[.//span[text()='All Calls']]")
        self.open_calls = (By.XPATH, "//ul[@role='listbox']//li[.//span[text()='Open Calls']]")
        self.closed_all = (By.XPATH, "//ul[@role='listbox']//li[.//span[text()='Closed Calls']]")
        self.all_tab = (By.XPATH, "//button[span[text()='All']]")
        self.buy_tab = (By.XPATH, "//button[span[text()='Buy']]")
        self.sell_tab = (By.XPATH, "//button[span[text()='Sell']]")
        self.fno_tab = (By.ID, "F&O")
        self.commodity_tab = (By.ID, 'Commodity')
        self.order_tab = (By.ID, "2_heade_tab")
        self.all_order = (By.XPATH, "//nav[@id='tab_navbar']//a[contains(text(), 'All')]")
        self.pending_order = (By.XPATH, "//nav[@id='tab_navbar']//a[contains(text(), 'Pending')]")
        self.executed_order = (By.XPATH, "//nav[@id='tab_navbar']//a[contains(text(), 'Executed')]")
        self.gtt_order = (By.XPATH, "//nav[@id='tab_navbar']//a[contains(text(), 'GTT')]")
        self.refresh_button = (By.XPATH, "//button[contains(text(), 'Refresh') and contains(@class, 'outlined_btn')]")
        self.position_tab = (By.ID, "3_heade_tab")
        self.holdings_tab = (By.ID, "4_heade_tab")
        self.funds_tab = (By.ID, "5_heade_tab")
        self.investment_label = (By.ID, "investment_label")
        self.current_value = (By.ID, "Current_value")
        self.profit_loss = (By.ID, "profit_loss")
        self.add_withdrawal_fund = (By.XPATH, "//button[contains(text(), 'Add/Withdraw Funds')]")
        self.funds_available = (
        By.XPATH, "//button[@type='button' and @class='cursor-pointer']/img[@alt='downExpandArrow']/parent::button")
        self.collateral_available = (
        By.XPATH, "//button[@type='button' and @class='cursor-pointer'][.//img[@alt='downExpandArrow']]")
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
        self.header_menu = (By.ID, "header_menu")
        self.profile = (By.XPATH,"//a[@role='option' and span[text()='Profile']]")
        self.reports = (By.XPATH,"//a[@role='option' and .//span[text()='Reports']]")
        self.settings = (By.XPATH, "//a[span[text()='Settings']]")
        self.checkbox_orderbook = (By.XPATH, "//tr[td//div[text()='IDEA-EQ']]//input[@type='checkbox']")
        self.orderbook_modify = (By.XPATH, "//tr[td//div[text()='IDEA-EQ']]//button[contains(text(), 'Modify')]")

        # self.need_help = (By.XPATH, "//a[@role='option' and .//span[text()='Help']]")
        # self.sign_out = (By.XPATH, "//a[@role='option' and .//span[text()='Sign out']]")

        # self.commodity_tab = (By.ID, "Commodity")

    def dashboard_header(self, test_results, expected="pass"):
        elements = [
            ("home_tab", self.home_tab),
            ("stock_holding", self.stock_holding),
            ("home_funds_label", self.home_funds_label),
            ("investment", self.investment),
            ("Current_value", self.Current_value),
            ("profit_loss", self.profit_loss),
            ("todays_pnl", self.todays_pnl),
            ("home_funds_label", self.home_funds_label),
            ("ava_label", self.ava_label),
            ("margin_used_label", self.margin_used_label),
            ("open_bal_label", self.open_bal_label),
            ("payIn_nav", self.payIn_nav),
            ("grobox_label", self.grobox_iifl),
            ("insta_options_label", self.insta_options),
            ("invest_stock_label", self.invest_stock_label),
            ("equities_ideas", self.equities_ideas),
            ("long_term", self.long_term),
            ("short_term", self.short_term),
            ("intraday", self.intraday),
            ("equity_drop_down_list", self.drop_down),
            ("all_calls", self.all_calls),
            # ("open_calls", self.open_calls),
            # ("closed_all", self.closed_all),
            ("all_tab", self.all_tab),
            ("buy_tab", self.buy_tab),
            ("sell_tab", self.sell_tab),
            ("fno_tab", self.fno_tab),
            ("commodity_tab", self.commodity_tab),
            ("order_tab", self.order_tab),
            ("all_order", self.all_order),
            ("pending_order", self.pending_order),
            ("executed_order", self.executed_order),
            ("gtt_order", self.gtt_order),
            ("refresh_button", self.refresh_button),
            ("position_tab", self.position_tab),
            ("holdings_tab", self.holdings_tab),
            ("funds_tab", self.funds_tab),
            ("investment_label", self.investment_label),
            ("current_value", self.current_value),
            ("profit_loss", self.profit_loss),
            ("add_withdrawal_fund", self.add_withdrawal_fund),
            ("funds_available", self.funds_available),
            ("collateral_available", self.collateral_available),
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
        elements_2 =[
            ("header_menu", self.header_menu),
            ("profile", self.profile),
            ("reports", self.reports),
            ("settings", self.settings),
            # ("need_help", self.need_help),
            # ("sign_out", self.sign_out),
        ]
        dropdown_options = [
            ("profile_option", lambda: self.driver.find_element(By.XPATH, "//a[@role='option' and span[text()='Profile']]")),
            ("reports_option", lambda: self.driver.find_element(By.XPATH, "//a[@role='option' and .//span[text()='Reports']]")),
            # ("settings_option", lambda: self.driver.find_element(By.XPATH, "//span[text()='Settings']/..")),
            # ("need_help_option", lambda: self.driver.find_element(By.XPATH, "//span[text()='Need Help']/..")),
            # ("signout_option", lambda: self.driver.find_element(By.XPATH, "//span[text()='Signout']/..")),
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
                "Page": "dashboard",
                "Testing_Area": name,
                "expected": expected,
                "actual": "clicked successfully" if status == "pass" else actual_error,
                "status": status
            })

            time.sleep(2)

        dropdown_options = [
            "Profile",
            "Reports",
            "Settings",
            "Need Help",
            "Sign out"
        ]

        for option_text in dropdown_options:
            name = f"{option_text.lower().replace(' ', '_')}_option"

            try:
                # Open the dropdown each time
                WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable(self.header_menu)
                ).click()
                time.sleep(1)

                # Locate the current option using visible text
                locator = (
                    By.XPATH,
                    f"//span[normalize-space(text())='{option_text}']/.."
                )

                WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable(locator)
                ).click()


                time.sleep(2)

                status = "pass"
                actual_error = ""
                print(f"{name} clicked successfully")

                test_results.append({
                    "Page": "dashboard",
                    "Testing_Area": name,
                    "expected": expected,
                    "actual": "clicked successfully" if status == "pass" else actual_error,
                    "status": status
                })

            except Exception as e:
                status = "fail"
                actual_error = str(e)
                print(f"{name} failed: {actual_error}")

            # test_results.append((name, status, actual_error))



        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable(self.drop_down)
        #     ).click()
        #     time.sleep(1)
        #
        #     dropdown_items = [
        #         ("all_calls", self.all_calls),
        #         ("open_calls", self.open_calls),
        #         ("closed_all", self.closed_all),
        #     ]
        #
        #     for name, item in dropdown_items:
        #         try:
        #             WebDriverWait(self.driver, 10).until(
        #                 EC.element_to_be_clickable(item)
        #             ).click()
        #             time.sleep(1)
        #             status = "pass"
        #             actual_error = ""
        #         except Exception as e:
        #             status = "fail"
        #             actual_error = "Dropdown item not clickable"
        #
        #         test_results.append({
        #             "watchlist_bottom_tab": name,
        #             "expected": expected,
        #             "actual": "clicked successfully" if status == "pass" else actual_error,
        #             "status": status
        #         })
        #
        #         # Click dropdown again if not the last item
        #         if name != "closed_all":
        #             WebDriverWait(self.driver, 10).until(
        #                 EC.element_to_be_clickable(self.drop_down)
        #             ).click()
        #             time.sleep(1)
        #
        # except Exception as e:
        #     test_results.append({
        #         "watchlist_bottom_tab": "drop_down_click",
        #         "expected": expected,
        #         "actual": "Dropdown button not found or not clickable",
        #         "status": "fail"
        #     })

    def get_login_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None
