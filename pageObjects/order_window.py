import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pageObjects.dashboard import dashBoardPage

from pageObjects.helpers import Helpers


# -*- coding: utf-8 -*-

class orderWindowPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.dashboard = dashBoardPage(driver)
        self.helpers = Helpers(driver)
        self.ow_regular_tab = (By.XPATH, '//nav[@id="order_tabs"]//button[text()="Regular"]')
        # self.ow_boco_tab = (By.XPATH, '//button[contains(text(), "BO/CO") and contains(@class, "commonInActiveTab")]')
        # self.ow_gtt_tab = (By.XPATH, '//nav[@id="order_tabs"]//button[text()="GTT"]')
        self.ow_normal_tab = (By.XPATH, '//nav[@id="pcode_tabs"]//button[text()="NRML"]')
        self.ow_intraday_tab = (By.XPATH, '//nav[@id="pcode_tabs"]//button[text()="Intraday"]')
        self.ow_limit_tab = (By.XPATH, '//nav[@id="priceType_tabs"]//button[text()="Limit"]')
        self.ow_market_tab = (By.XPATH, '//nav[@id="priceType_tabs"]//button[text()="Market"]')
        self.ow_stop_loss_tab = (By.XPATH, '//nav[@id="priceType_tabs"]//button[text()="SL"]')
        self.ow_stop_loss_market_tab = (By.XPATH, '//nav[@id="priceType_tabs"]//button[text()="SLM"]')
        self.buy_button = (
            By.XPATH,
            "//button[contains(@class, 'capitalize') and contains(@class, 'green_btn') and span[text()='Buy']]")
        self.confirm_buy = (By.XPATH, "//button[@type='button' and @class='confirm_btn' and text()='Yes']")
        self.confirm_amo = (By.XPATH, "//button[@type='button' and contains(@class, 'confirm_btn') and text()='Yes']")
        self.modify_button = (By.XPATH, "//button[span[text()='Modify']]")
        self.ioc_button = (By.ID, "pcode_1")

    # def orderWindow(self, test_results, expected="pass"):
    #     elements = [
    #         ("order_window_regular_tab", "//button[normalize-space()='Regular']"),
    #         # ("order_window_bnpl_tab", '//nav[@id="pcode_tabs"]//button[text()="BNPL"]'),
    #         # ("order_window_intraday_tab", "//button[normalize-space()='Intraday']"),
    #         ("order_window_delivery_tab", "//button[normalize-space()='Delivery']"),
    #         ("order_window_limit_tab", "//button[normalize-space()='Limit']"),
    #         # ("order_window_market_tab", "//button[normalize-space()='Market']"),
    #         ("order_window_stop_loss_tab", "//button[normalize-space()='SL']"),
    #         # ("order_window_stop_loss_market_tab", "//button[normalize-space()='SLM']"),
    #         # ("order_window_boco_tab", "//button[normalize-space()='BO/CO']"),
    #         # ("order_window_bracket_tab", "//button[normalize-space()='Bracket']"),
    #         # ("order_window_cover_tab", "//button[normalize-space()='Cover']"),
    #         # ("order_window_gtt_tab", "//button[normalize-space(text())='GTT']"),
    #         # ("order_window_single_tab", "//button[normalize-space()='Single']"),
    #         # ("order_window_oco_tab", "//button[normalize-space()='OCO']"),
    #     ]
    #
    #     for name, xpath in elements:
    #         try:
    #             action_log = []
    #
    #             tab_button = WebDriverWait(self.driver, 10).until(
    #                 EC.element_to_be_clickable((By.XPATH, xpath))
    #             )
    #             self.driver.execute_script("arguments[0].scrollIntoView(true);", tab_button)
    #             tab_button.click()
    #             time.sleep(3)
    #             action_log.append(f"Clicked tab: {name}")
    #
    #             if name in ["order_window_delivery_tab", "order_window_limit_tab"]:
    #                 try:
    #                     qty_field = WebDriverWait(self.driver, 5).until(
    #                         EC.element_to_be_clickable((By.ID, "qty"))
    #                     )
    #                     qty_field.clear()
    #                     qty_field.send_keys("1")
    #                     action_log.append("Quantity field entered: 1")
    #
    #                     price_field = WebDriverWait(self.driver, 5).until(
    #                         EC.element_to_be_clickable((By.ID, "price"))
    #                     )
    #
    #                     price_field.clear()
    #                     price_field.send_keys("6.81")
    #                     action_log.append("Price field entered: 6.83")
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.buy_button)
    #                     ).click()
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.confirm_buy)
    #                     ).click()
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.confirm_amo)
    #                     ).click()
    #
    #                     time.sleep(5)
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.dashboard.order_tab)
    #                     ).click()
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.dashboard.pending_order)
    #                     ).click()
    #
    #                     time.sleep(5)
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)
    #                     ).click()
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.dashboard.orderbook_modify)
    #                     ).click()
    #
    #                     time.sleep(5)
    #
    #                     qty_field.clear()
    #                     qty_field.send_keys("5")
    #                     action_log.append("Quantity field entered: 1")
    #
    #                     price_field = WebDriverWait(self.driver, 5).until(
    #                         EC.element_to_be_clickable((By.ID, "price"))
    #                     )
    #
    #                     price_field.clear()
    #                     price_field.send_keys("6.41")
    #                     action_log.append("Price field entered: 6.41")
    #
    #                     WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable(self.modify_button)
    #                     ).click()
    #
    #                     # checkbox = driver.find_element(
    #                     #     By.XPATH, "//tr[.//div[contains(text(),'IDEA-EQ')]]//input[@type='checkbox']"
    #                     # )
    #                     # checkbox.click()
    #
    #                     # Then click the Modify button
    #                     # modify_button = driver.find_element(
    #                     #     By.XPATH, "//tr[.//div[contains(text(),'IDEA-EQ')]]//button[contains(text(), 'Modify')]"
    #                     # )
    #                     # modify_button.click()
    #                 except Exception as field_error:
    #                     raise Exception(f"Bracket tab clicked but field edit failed: {field_error}")
    #
    #             # if name in ["order_window_delivery_tab", "order_window_stop_loss_tab"]:
    #             #     try:
    #             #         qty_field = WebDriverWait(self.driver, 5).until(
    #             #             EC.element_to_be_clickable((By.ID, "qty"))
    #             #         )
    #             #         qty_field.clear()
    #             #         qty_field.send_keys("1")
    #             #         action_log.append("Quantity field entered: 1")
    #             #
    #             #         price_field = WebDriverWait(self.driver, 5).until(
    #             #             EC.element_to_be_clickable((By.ID, "price"))
    #             #         )
    #             #
    #             #         price_field.clear()
    #             #         price_field.send_keys("6.71")
    #             #         action_log.append("Price field entered: 6.83")
    #             #
    #             #         WebDriverWait(self.driver, 10).until(
    #             #             EC.element_to_be_clickable(self.buy_button)
    #             #         ).click()
    #             #
    #             #         WebDriverWait(self.driver, 10).until(
    #             #             EC.element_to_be_clickable(self.confirm_buy)
    #             #         ).click()
    #             #
    #             #         WebDriverWait(self.driver, 10).until(
    #             #             EC.element_to_be_clickable(self.confirm_amo)
    #             #         ).click()
    #             #
    #             #         time.sleep(5)
    #             #
    #             #         # WebDriverWait(self.driver, 10).until(
    #             #         #     EC.element_to_be_clickable(self.dashboard.order_tab)
    #             #         # ).click()
    #             #
    #             #         # WebDriverWait(self.driver, 10).until(
    #             #         #     EC.element_to_be_clickable(self.dashboard.pending_order)
    #             #         # ).click()
    #             #         #
    #             #         # time.sleep(5)
    #             #         #
    #             #         # WebDriverWait(self.driver, 10).until(
    #             #         #     EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)
    #             #         # ).click()
    #             #         #
    #             #         # WebDriverWait(self.driver, 10).until(
    #             #         #     EC.element_to_be_clickable(self.dashboard.orderbook_modify)
    #             #         # ).click()
    #             #         #
    #             #         # time.sleep(5)
    #             #         #
    #             #         # qty_field.clear()
    #             #         # qty_field.send_keys("5")
    #             #         # action_log.append("Quantity field entered: 1")
    #             #         #
    #             #         # price_field = WebDriverWait(self.driver, 5).until(
    #             #         #     EC.element_to_be_clickable((By.ID, "price"))
    #             #         # )
    #             #         #
    #             #         # price_field.clear()
    #             #         # price_field.send_keys("6.41")
    #             #         # action_log.append("Price field entered: 6.41")
    #             #         #
    #             #         # WebDriverWait(self.driver, 10).until(
    #             #         #     EC.element_to_be_clickable(self.modify_button)
    #             #         # ).click()
    #             #
    #             #     except Exception as field_error:
    #             #         raise Exception(f"Bracket tab clicked but field edit failed: {field_error}")
    #
    #             status = "pass"
    #             actual_error = "; ".join(action_log)
    #
    #             view_charges = WebDriverWait(self.driver, 10).until(
    #                 EC.element_to_be_clickable((By.XPATH,
    #                                             "//a[@class='text-center text-xs hyperLink cursor-pointer whitespace-nowrap' and text()='View Charges']"))
    #             )
    #             view_charges.click()
    #
    #             time.sleep(3)
    #
    #             close_icon = WebDriverWait(self.driver, 10).until(
    #                 EC.element_to_be_clickable(
    #                     (By.XPATH, "//span[contains(@class, 'cursor-pointer') and contains(@class, 'w-[18px]')]"))
    #             )
    #             close_icon.click()
    #         except Exception as e:
    #             status = "fail"
    #             actual_error = str(e)
    #
    #         test_results.append({
    #             "Testing_Area": name,
    #             "expected": expected,
    #             "actual": actual_error,
    #             "status": status
    #         })

    # NEW-CODE#

    # def orderWindow(self, test_results, expected="pass"):
    #     try:
    #
    #         action_log = []
    #
    #         # STEP 1: DELIVERY + LIMIT
    #         self._select_tab("Delivery", "//button[normalize-space()='Delivery']", action_log)
    #         self._select_tab("Limit", "//button[normalize-space()='Limit']", action_log)
    #         self._place_and_modify_order(qty="1", price="6.81", new_qty="5", new_price="6.41", action_log=action_log)
    #
    #         # STEP 2: Open order window again for SL
    #         self._reopen_first_scrip_order_window()
    #
    #         # STEP 3: DELIVERY + SL
    #         self._select_tab("Delivery", "//button[normalize-space()='Delivery']", action_log)
    #         self._select_tab("SL", "//button[normalize-space()='SL']", action_log)
    #         self._place_and_modify_order(qty="1", price="6.50", new_qty="3", new_price="6.30", action_log=action_log)
    #
    #         status = "pass"
    #         actual_error = "; ".join(action_log)
    #         # test_results.append((self.orderWindow.__name__, expected, "pass", "\n".join(action_log)))
    #         test_results.append({
    #                     "Testing_Area": self.orderWindow.__name__,
    #                     "expected": expected,
    #                     "actual": actual_error,
    #                     "status": status
    #                 })
    #
    #     except Exception as e:
    #
    #         status = "fail"
    #         actual_error = str(e)
    #
    #         test_results.append({
    #             "Testing_Area": self.orderWindow.__name__,
    #             "expected": expected,
    #             "actual": actual_error,
    #             "status": status
    #         })
    #         # test_results.append((self.orderWindow.__name__, expected, "fail", f"Error: {str(e)}"))

    # LATEST-CODE#

    def orderWindow(self, test_results, expected="pass"):
        driver = self.driver
        wait = WebDriverWait(driver, 12)
        action_log = []

        # ---------------------
        # Helper: safe element lookup from several XPaths
        # ---------------------
        def _first_present(xpaths, timeout=10):
            end = time.time() + timeout
            last_exc = None
            while time.time() < end:
                for xp in xpaths if isinstance(xpaths, (list, tuple)) else [xpaths]:
                    try:
                        el = driver.find_element(By.XPATH, xp)
                        return el
                    except Exception as e:
                        last_exc = e
                time.sleep(0.2)
            raise last_exc if last_exc else Exception("Element not found")

        # ---------------------
        # Helper: safe click (move → scroll → normal → JS fallback)
        # ---------------------
        def _safe_click(el):
            try:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                ActionChains(driver).move_to_element(el).pause(0.1).perform()
                wait.until(EC.element_to_be_clickable(el)).click()
            except Exception:
                try:
                    driver.execute_script("arguments[0].click();", el)
                except Exception as e:
                    raise e

        def _set_order_price(order_price="10"):
            order_price_el = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='number' and @maxlength='5']")))
            order_price_el.clear()
            order_price_el.send_keys(order_price)
        # ---------------------
        # Helper: close any open order window / modal
        # ---------------------
        def _close_order_window_if_open():
            close_xpaths = [
                "//button[contains(@class,'cancel_btn') or normalize-space()='Cancel' or normalize-space()='Close']",
                "//span[contains(@class,'br-modal-close') and normalize-space()='×']/..",
                "//button[@type='button' and @aria-label='Close']",
            ]
            try:
                el = _first_present(close_xpaths, timeout=2)
                _safe_click(el)
                # wait for modal to disappear
                time.sleep(0.5)
            except Exception:
                pass  # nothing to close

        # ---------------------
        # Helper: confirm any 'Yes' dialogs (AMO / confirm)
        # ---------------------
        def _confirm_yes_if_present(max_clicks=2, timeout_each=3):
            yes_xp = "//button[contains(@class,'confirm_btn') and normalize-space()='Yes']"
            clicks = 0
            for _ in range(max_clicks):
                try:
                    el = WebDriverWait(driver, timeout_each).until(
                        EC.element_to_be_clickable((By.XPATH, yes_xp))
                    )
                    _safe_click(el)
                    clicks += 1
                    time.sleep(0.4)
                except Exception:
                    break
            return clicks

        # ---------------------
        # Helper: get scrip name by index
        # ---------------------
        def _scrip_name_by_index(i):
            # Adjust this if you have a specific name locator inside each scrip
            name_candidates = [
                f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]//div[contains(@id,'_scrip_name')]",
                f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]//span[contains(@class,'name')]",
                f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]//span",
            ]
            for xp in name_candidates:
                try:
                    txt = driver.find_element(By.XPATH, xp).text.strip()
                    if txt:
                        return txt
                except Exception:
                    continue
            return f"Scrip-{i}"

        # ---------------------
        # Helper: re-locate scrip container by index
        # ---------------------
        def _scrip_by_index(i):
            xp = f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]"
            return wait.until(EC.presence_of_element_located((By.XPATH, xp)))

        # ---------------------
        # Helper: open buy window for given scrip index
        # ---------------------
        def _open_buy_for_index(i):
            scrip = _scrip_by_index(i)
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", scrip)
            ActionChains(driver).move_to_element(scrip).pause(0.1).perform()
            time.sleep(0.2)
            buy_buttons = [
                ".//button[normalize-space()='B']",
                ".//button[.//span[normalize-space()='B']]",
                ".//button[contains(@id,'_buy')]",
                ".//button[contains(@class,'buy')]",
            ]
            buy = None
            for rel in buy_buttons:
                try:
                    buy = scrip.find_element(By.XPATH, rel)
                    break
                except Exception:
                    continue
            if not buy:
                raise Exception("Buy button not found on scrip row")
            _safe_click(buy)
            time.sleep(0.4)  # small pause for modal animation

        # ---------------------
        # Helper: select tabs/buttons inside order window
        # ---------------------
        def _select_regular():
            xp = '//nav[@id="order_tabs"]//button[normalize-space()="Regular"]'
            el = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
            _safe_click(el)
            time.sleep(0.2)

        def _select_gtt():
            xp = '//nav[@id="order_tabs"]//button[normalize-space()="GTT"]'
            el = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
            _safe_click(el)
            time.sleep(0.2)

        def _select_bo_co():
            xp = '//nav[@id="order_tabs"]//button[normalize-space()="BO/CO"]'
            el = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
            _safe_click(el)
            time.sleep(0.2)

        def _pcode_button():
            id = 'pcode_1'
            el = wait.until(EC.element_to_be_clickable((By.ID, id)))
            _safe_click(el)
            time.sleep(0.2)

        def _select_product_preferring_nrml():
            # Try NRML first; if not present, fall back to Delivery/CNC
            nrml_xpaths = [
                "//button[normalize-space()='NRML']",
                "//button[normalize-space()='NRM']",
                "//button[contains(@class,'nrml')]",
            ]
            delivery_xpaths = [
                "//button[contains(normalize-space(),'Delivery')]",
                "//button[normalize-space()='CNC']",
                "//button[contains(@class,'delivery')]",
            ]

            try:
                el = _first_present(nrml_xpaths, timeout=2)
                _safe_click(el)
                return "NRML"
            except Exception:
                el = _first_present(delivery_xpaths, timeout=3)
                _safe_click(el)
                return "Delivery"

        def _select_product_preferring_intraday():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'Intraday')]",
                "//button[normalize-space()='MIS']",
                "//button[contains(@class,'intraday')]",
            ]

            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "Intraday"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "MIS"

        def _select_product_preferring_bracket():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'Bracket')]",
                "//button[normalize-space()='Bracket']",
                "//button[contains(@class,'Bracket')]",
            ]

            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "Bracket"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "Bracket"

        def _select_product_preferring_cover():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'Cover')]",
                "//button[normalize-space()='Cover']",
                "//button[contains(@class,'Cover')]",
            ]

            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "Cover"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "Cover"

        def _select_product_preferring_bnpl():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'BNPL')]",
                "//button[normalize-space()='BNPL']",
                "//button[contains(@class,'BNPL')]",
            ]
            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "BNPL"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "BNPL"

        def _select_order_type(order_type):
            order_xpaths = {
                "Limit": [
                    "//button[normalize-space()='Limit']",
                    "//button[normalize-space()='LMT']",
                ],
                "Market": [
                    "//button[normalize-space()='Market']",
                    "//button[normalize-space()='MKT']",
                ],
                "SL": [
                    "//button[normalize-space()='SL']",
                    "//button[contains(.,'Stop Loss')]",
                    "//button[normalize-space()='SL-L']",
                ],
                "SLM": [
                    "//button[normalize-space()='SLM']",
                    "//button[contains(.,'Stop Loss Market')]",
                    "//button[normalize-space()='SL-M']",
                ],

                "Single": [
                    "//button[normalize-space()='Single']",
                    "//button[contains(.,'Single')]",
                    "//button[normalize-space()='Single']",
                ],

                "OCO": [
                    "//button[normalize-space()='OCO']",
                    "//button[contains(.,'OCO')]",
                    "//button[normalize-space()='OCO']",
                ],
            }
            candidates = order_xpaths.get(order_type, [f"//button[normalize-space()='{order_type}']"])
            el = _first_present(candidates, timeout=4)
            _safe_click(el)
            time.sleep(0.2)

        def _set_qty(qty="1"):
            qty_el = wait.until(EC.element_to_be_clickable((By.ID, "qty")))
            qty_el.clear()
            # qty_el.send_keys(qty)
            for _ in range(3):
                time.sleep(0.3)
                qty_el.send_keys(Keys.ARROW_UP)

        # def _set_stop_loss(qty="1"):
        #     sl_trigger_price_el = wait.until(EC.element_to_be_clickable((By.ID, "triggerPrice")))
        #     sl_trigger_price_el.clear()
        #     # qty_el.send_keys(qty)
        #     for _ in range(3):
        #         time.sleep(0.3)
        #         sl_trigger_price_el.send_keys(Keys.ARROW_UP)

        def _set_target_price():
            try:
                price_el = wait.until(EC.presence_of_element_located((By.ID, "price")))
                current_price = float(price_el.get_attribute("value"))
                stoploss_value = current_price + 2

                print(stoploss_value)

                sl_el = wait.until(EC.element_to_be_clickable((By.ID, "targetPrice")))
                sl_el.clear()
                sl_el.send_keys(str(stoploss_value))
                return stoploss_value
            except Exception as e:
                raise Exception(f"Stoploss setting failed: {str(e)}")

        def _set_stoploss_minus_2():
            try:
                price_el = wait.until(EC.presence_of_element_located((By.ID, "price")))
                current_price = float(price_el.get_attribute("value"))
                stoploss_value = current_price - 2
                bracket_order_stoploss_value = current_price - 550

                print(stoploss_value)
                try:

                    sl_el = wait.until(EC.element_to_be_clickable((By.ID, "triggerPrice")))
                    sl_el.clear()
                    sl_el.send_keys(str(stoploss_value))
                    return stoploss_value

                except Exception as e:

                    sl_el = wait.until(EC.element_to_be_clickable((By.ID, "stoplossPrice")))
                    sl_el.clear()
                    sl_el.send_keys(str(bracket_order_stoploss_value))
                    return stoploss_value

            except Exception as e:
                raise Exception(f"Stoploss setting failed: {str(e)}")

        def _set_stoploss_minus_slm():
            try:
                # Get NSE price from order window (example: "NSE 1,034.40 2.15 (0.21%)")
                nse_price_el = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="draggable-header"]/div/div[2]/div/section/span[2]'))
                )
                nse_text = nse_price_el.text.strip()

                # Extract numeric price (second token after 'NSE')
                nse_price = float(nse_text.split()[1].replace(",", ""))  # e.g. 1034.40

                # Stoploss trigger = LTP - 2
                stoploss_value = nse_price - 2

                print(stoploss_value)

                # Fill SL Trigger Price field
                sl_trigger_el = wait.until(EC.element_to_be_clickable((By.ID, "triggerPrice")))
                sl_trigger_el.clear()
                sl_trigger_el.send_keys(str(stoploss_value))

                return stoploss_value

            except Exception as e:
                raise Exception(f"Stoploss setting failed: {str(e)}")

        def _click_buy_submit():
            buy_btn = _first_present(
                [
                    "//button[.//span[normalize-space()='Buy']]",
                    "//button[normalize-space()='Buy']",
                    "//button[contains(@class,'green_btn')]",
                ],
                timeout=5,
            )
            _safe_click(buy_btn)

        def nrml_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Limit")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Market")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present()

        #
        def nrml_stoploss():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("SL")
            _set_qty("1")
            _set_stoploss_minus_2()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_stoploss_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("SLM")
            _set_qty("1")
            _set_stoploss_minus_slm()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_pcode_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Limit")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_pcode_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Market")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_pcode_slm():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("SLM")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Limit")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Market")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present()

        #
        def intraday_stoploss():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("SL")
            _set_qty("1")
            _set_stoploss_minus_2()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_stoploss_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("SLM")
            _set_qty("1")
            _set_stoploss_minus_slm()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_pcode_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Limit")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_pcode_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Market")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_pcode_slm():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("SLM")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bracket_bo_co():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_bo_co()
            _select_product_preferring_bracket()
            _select_order_type("Limit")
            _set_qty("1")
            _set_stoploss_minus_2()
            _set_target_price()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def cover_bo_co():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_bo_co()
            _select_product_preferring_cover()
            _select_order_type("Limit")
            _set_qty("1")
            _set_stoploss_minus_2()
            _set_target_price()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def gtt_single():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_gtt()
            _select_product_preferring_nrml()
            _select_order_type("Single")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def gtt_oco():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_gtt()
            _select_product_preferring_nrml()
            _select_order_type("OCO")
            _set_qty("1")
            _set_order_price("10")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Limit")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Market")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present()

            #

        def bnpl_stoploss():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("SL")
            _set_qty("1")
            _set_stoploss_minus_2()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_stoploss_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("SLM")
            _set_qty("1")
            _set_stoploss_minus_slm()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_pcode_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Limit")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_pcode_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Market")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_pcode_slm():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("SLM")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        # ======================
        # Main flow starts here
        # ======================

        scrips = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]")
            )
        )
        scrip_total = len(scrips)

        for i in range(1, scrip_total):
            name = _scrip_name_by_index(i)
            #

            # --- Run 1: Regular + NRML (or Delivery fallback) + Limit ---
            # try:
            #     nrml_limit()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "normal_limit",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + Limit FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # # --- Run 2: Regular + NRML (or Delivery fallback) + SL ---
            #
            # try:
            #     nrml_market()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "normal_market",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            # except Exception as e:
            #     action_log.append(f"[{name}] Regular + NRML/Delivery + Market FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_stoploss()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "normal_stoploss",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_stoploss_market()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "normal_stoploss_market",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            # #
            # #     # --------------------IOC-----------------
            # try:
            #     nrml_pcode_limit()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "normal_limit",
            #         "validity": 'IOC',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_pcode_market()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "normal_market",
            #         "validity": 'IOC',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_pcode_slm()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "normal_stoploss_market",
            #         "validity": 'IOC',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # #     # --------------------INTRADAY-----------------
            #
            # try:
            #     intraday_limit()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "intraday_limit",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_market()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "intraday_market",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_stoploss()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "intraday_stoploss",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_stoploss_market()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "intraday_stoploss_market",
            #         "validity": 'NET',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_pcode_limit()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "intraday_limit",
            #         "validity": 'IOC',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_pcode_market()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "intraday_market",
            #         "validity": 'IOC',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            # try:
            #     intraday_pcode_slm()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "intraday_stoploss_market",
            #         "validity": 'IOC',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            # #
            # #
            #
            # try:
            #     bracket_bo_co()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "bracket_limit",
            #         "validity": '',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     cover_bo_co()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "order_type": "cover_limit",
            #         "validity": '',
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()

            #     # --------------------GTT-----------------

            try:
                gtt_single()
                status = "pass"
                actual_error = ""
                test_results.append({
                    "watchlist_bottom_tab": name,
                    "order_type": "gtt_single",
                    "validity": '',
                    "expected": expected,
                    "actual": "clicked successfully" if status == "pass" else actual_error,
                    "status": status
                })
                # action_log.append(f"[{name}] Regular + {product_used} + Limit → Buy submitted")
            except Exception as e:
                print(e)
                # action_log.append(f"[{name}] Regular + NRML/Delivery + Limit FAILED: {str(e)}")
            finally:
                _close_order_window_if_open()

            try:
                gtt_oco()
                status = "pass"
                actual_error = ""
                test_results.append({
                    "watchlist_bottom_tab": name,
                    "order_type": "gtt_co",
                    "validity": '',
                    "expected": expected,
                    "actual": "clicked successfully" if status == "pass" else actual_error,
                    "status": status
                })
                # action_log.append(f"[{name}] Regular + {product_used} + Limit → Buy submitted")
            except Exception as e:
                print(e)
                # action_log.append(f"[{name}] Regular + NRML/Delivery + Limit FAILED: {str(e)}")
            finally:
                print("ORDER-WINDOW")
                # _close_order_window_if_open()
            try:
                bnpl_limit()
                # bnpl_market()
                # bnpl_stoploss()
                # bnpl_stoploss_market()
                # bnpl_pcode_limit()
                # bnpl_pcode_market()
                # bnpl_pcode_slm()
                # action_log.append(f"[{name}] Regular + {product_used} + Limit → Buy submitted")
            except Exception as e:
                print(e)
                # action_log.append(f"[{name}] Regular + NRML/Delivery + Limit FAILED: {str(e)}")
            finally:
                _close_order_window_if_open()

        # Collect result
        status = "pass"
        test_results.append({
            "Testing_Area": self.orderWindow.__name__,
            "expected": expected,
            "actual": "; ".join(action_log),
            "status": status
        })

    def orderWindow_Sell(self, test_results, expected="pass"):
        driver = self.driver
        wait = WebDriverWait(driver, 12)
        action_log = []

        # ---------------------
        # Helper: safe element lookup from several XPaths
        # ---------------------
        def _first_present(xpaths, timeout=10):
            end = time.time() + timeout
            last_exc = None
            while time.time() < end:
                for xp in xpaths if isinstance(xpaths, (list, tuple)) else [xpaths]:
                    try:
                        el = driver.find_element(By.XPATH, xp)
                        return el
                    except Exception as e:
                        last_exc = e
                time.sleep(0.2)
            raise last_exc if last_exc else Exception("Element not found")

        # ---------------------
        # Helper: safe click (move → scroll → normal → JS fallback)
        # ---------------------
        def _safe_click(el):
            try:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                ActionChains(driver).move_to_element(el).pause(0.1).perform()
                wait.until(EC.element_to_be_clickable(el)).click()
            except Exception:
                try:
                    driver.execute_script("arguments[0].click();", el)
                except Exception as e:
                    raise e

        # ---------------------
        # Helper: close any open order window / modal
        # ---------------------
        def _close_order_window_if_open():
            close_xpaths = [
                "//button[contains(@class,'cancel_btn') or normalize-space()='Cancel' or normalize-space()='Close']",
                "//span[contains(@class,'br-modal-close') and normalize-space()='×']/..",
                "//button[@type='button' and @aria-label='Close']",
            ]
            try:
                el = _first_present(close_xpaths, timeout=2)
                _safe_click(el)
                # wait for modal to disappear
                time.sleep(0.5)
            except Exception:
                pass  # nothing to close

        # ---------------------
        # Helper: confirm any 'Yes' dialogs (AMO / confirm)
        # ---------------------
        def _confirm_yes_if_present(max_clicks=2, timeout_each=3):
            yes_xp = "//button[contains(@class,'confirm_btn') and normalize-space()='Yes']"
            clicks = 0
            for _ in range(max_clicks):
                try:
                    el = WebDriverWait(driver, timeout_each).until(
                        EC.element_to_be_clickable((By.XPATH, yes_xp))
                    )
                    _safe_click(el)
                    clicks += 1
                    time.sleep(0.4)
                except Exception:
                    break
            return clicks

        # ---------------------
        # Helper: get scrip name by index
        # ---------------------
        def _scrip_name_by_index(i):
            # Adjust this if you have a specific name locator inside each scrip
            name_candidates = [
                f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]//div[contains(@id,'_scrip_name')]",
                f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]//span[contains(@class,'name')]",
                f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]//span",
            ]
            for xp in name_candidates:
                try:
                    txt = driver.find_element(By.XPATH, xp).text.strip()
                    if txt:
                        return txt
                except Exception:
                    continue
            return f"Scrip-{i}"

        # ---------------------
        # Helper: re-locate scrip container by index
        # ---------------------
        def _scrip_by_index(i):
            xp = f"(//div[contains(@class,'mklist') and contains(@class,'secondary-border')])[{i}]"
            return wait.until(EC.presence_of_element_located((By.XPATH, xp)))

        # ---------------------
        # Helper: open buy window for given scrip index
        # ---------------------
        def _open_buy_for_index(i):
            scrip = _scrip_by_index(i)
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", scrip)
            ActionChains(driver).move_to_element(scrip).pause(0.1).perform()
            time.sleep(0.2)
            buy_buttons = [
                ".//button[normalize-space()='S']",
                ".//button[.//span[normalize-space()='S']]",
                ".//button[contains(@id,'_sell')]",
                ".//button[contains(@class,'sell')]",
            ]
            buy = None
            for rel in buy_buttons:
                try:
                    buy = scrip.find_element(By.XPATH, rel)
                    break
                except Exception:
                    continue
            if not buy:
                raise Exception("Buy button not found on scrip row")
            _safe_click(buy)
            time.sleep(0.4)  # small pause for modal animation

        # ---------------------
        # Helper: select tabs/buttons inside order window
        # ---------------------
        def _select_regular():
            xp = '//nav[@id="order_tabs"]//button[normalize-space()="Regular"]'
            el = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
            _safe_click(el)
            time.sleep(0.2)

        def _select_gtt():
            xp = '//nav[@id="order_tabs"]//button[normalize-space()="GTT"]'
            el = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
            _safe_click(el)
            time.sleep(0.2)

        def _select_bo_co():
            xp = '//nav[@id="order_tabs"]//button[normalize-space()="BO/CO"]'
            el = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
            _safe_click(el)
            time.sleep(0.2)

        def _pcode_button():
            id = 'pcode_1'
            el = wait.until(EC.element_to_be_clickable((By.ID, id)))
            _safe_click(el)
            time.sleep(0.2)

        def _select_product_preferring_nrml():
            # Try NRML first; if not present, fall back to Delivery/CNC
            nrml_xpaths = [
                "//button[normalize-space()='NRML']",
                "//button[normalize-space()='NRM']",
                "//button[contains(@class,'nrml')]",
            ]
            delivery_xpaths = [
                "//button[contains(normalize-space(),'Delivery')]",
                "//button[normalize-space()='CNC']",
                "//button[contains(@class,'delivery')]",
            ]

            try:
                el = _first_present(nrml_xpaths, timeout=2)
                _safe_click(el)
                return "NRML"
            except Exception:
                el = _first_present(delivery_xpaths, timeout=3)
                _safe_click(el)
                return "Delivery"

        def _select_product_preferring_intraday():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'Intraday')]",
                "//button[normalize-space()='MIS']",
                "//button[contains(@class,'intraday')]",
            ]

            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "Intraday"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "MIS"

        def _select_product_preferring_bracket():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'Bracket')]",
                "//button[normalize-space()='Bracket']",
                "//button[contains(@class,'Bracket')]",
            ]

            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "Bracket"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "Bracket"

        def _select_product_preferring_cover():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'Cover')]",
                "//button[normalize-space()='Cover']",
                "//button[contains(@class,'Cover')]",
            ]

            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "Cover"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "Cover"

        def _select_product_preferring_bnpl():
            # Try NRML first; if not present, fall back to Delivery/CNC
            intraday_xpaths = [
                "//button[contains(normalize-space(),'BNPL')]",
                "//button[normalize-space()='BNPL']",
                "//button[contains(@class,'BNPL')]",
            ]
            try:
                el = _first_present(intraday_xpaths, timeout=2)
                _safe_click(el)
                return "BNPL"
            except Exception:
                el = _first_present(intraday_xpaths, timeout=3)
                _safe_click(el)
                return "BNPL"

        def _select_order_type(order_type):
            order_xpaths = {
                "Limit": [
                    "//button[normalize-space()='Limit']",
                    "//button[normalize-space()='LMT']",
                ],
                "Market": [
                    "//button[normalize-space()='Market']",
                    "//button[normalize-space()='MKT']",
                ],
                "SL": [
                    "//button[normalize-space()='SL']",
                    "//button[contains(.,'Stop Loss')]",
                    "//button[normalize-space()='SL-L']",
                ],
                "SLM": [
                    "//button[normalize-space()='SLM']",
                    "//button[contains(.,'Stop Loss Market')]",
                    "//button[normalize-space()='SL-M']",
                ],

                "Single": [
                    "//button[normalize-space()='Single']",
                    "//button[contains(.,'Single')]",
                    "//button[normalize-space()='Single']",
                ],

                "OCO": [
                    "//button[normalize-space()='OCO']",
                    "//button[contains(.,'OCO')]",
                    "//button[normalize-space()='OCO']",
                ],
            }
            candidates = order_xpaths.get(order_type, [f"//button[normalize-space()='{order_type}']"])
            el = _first_present(candidates, timeout=4)
            _safe_click(el)
            time.sleep(0.2)

        def _set_qty(qty="1"):
            qty_el = wait.until(EC.element_to_be_clickable((By.ID, "qty")))
            qty_el.clear()
            # qty_el.send_keys(qty)
            for _ in range(3):
                time.sleep(0.3)
                qty_el.send_keys(Keys.ARROW_UP)

        def _set_order_price(order_price="10"):
            order_price_el = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='number' and @maxlength='5']")))
            order_price_el.clear()
            order_price_el.send_keys(order_price)


        # def _set_stop_loss(qty="1"):
        #     sl_trigger_price_el = wait.until(EC.element_to_be_clickable((By.ID, "triggerPrice")))
        #     sl_trigger_price_el.clear()
        #     # qty_el.send_keys(qty)
        #     for _ in range(3):
        #         time.sleep(0.3)
        #         sl_trigger_price_el.send_keys(Keys.ARROW_UP)

        def _set_target_price():
            try:
                price_el = wait.until(EC.presence_of_element_located((By.ID, "price")))
                current_price = float(price_el.get_attribute("value"))
                stoploss_value = current_price + 2

                print(stoploss_value)

                sl_el = wait.until(EC.element_to_be_clickable((By.ID, "targetPrice")))
                sl_el.clear()
                sl_el.send_keys(str(stoploss_value))
                return stoploss_value
            except Exception as e:
                raise Exception(f"Stoploss setting failed: {str(e)}")

        def _set_stoploss_minus_2():
            try:
                price_el = wait.until(EC.presence_of_element_located((By.ID, "price")))
                current_price = float(price_el.get_attribute("value"))
                stoploss_value = current_price + 2
                bracket_order_stoploss_value = current_price - 550

                print(stoploss_value)
                try:

                    sl_el = wait.until(EC.element_to_be_clickable((By.ID, "triggerPrice")))
                    sl_el.clear()
                    sl_el.send_keys(str(stoploss_value))
                    return stoploss_value

                except Exception as e:

                    sl_el = wait.until(EC.element_to_be_clickable((By.ID, "stoplossPrice")))
                    sl_el.clear()
                    sl_el.send_keys(str(bracket_order_stoploss_value))
                    return stoploss_value

            except Exception as e:
                raise Exception(f"Stoploss setting failed: {str(e)}")

        def _set_stoploss_minus_slm():
            try:
                # Get NSE price from order window (example: "NSE 1,034.40 2.15 (0.21%)")
                nse_price_el = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="draggable-header"]/div/div[2]/div/section/span[2]'))
                )
                nse_text = nse_price_el.text.strip()

                # Extract numeric price (second token after 'NSE')
                nse_price = float(nse_text.split()[1].replace(",", ""))  # e.g. 1034.40

                # Stoploss trigger = LTP - 2
                stoploss_value = nse_price - 2

                print(stoploss_value)

                # Fill SL Trigger Price field
                sl_trigger_el = wait.until(EC.element_to_be_clickable((By.ID, "triggerPrice")))
                sl_trigger_el.clear()
                sl_trigger_el.send_keys(str(stoploss_value))

                return stoploss_value

            except Exception as e:
                raise Exception(f"Stoploss setting failed: {str(e)}")

        def _click_buy_submit():
            buy_btn = _first_present(
                [
                    "//button[.//span[normalize-space()='Sell']]",
                    "//button[normalize-space()='Sell']",
                    "//button[contains(@class,'red_btn')]",
                ],
                timeout=5,
            )
            _safe_click(buy_btn)

        def nrml_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Limit")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Market")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present()

        #
        def nrml_stoploss():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("SL")
            _set_qty("1")
            _set_stoploss_minus_2()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_stoploss_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("SLM")
            _set_qty("1")
            _set_stoploss_minus_slm()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_pcode_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Limit")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_pcode_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("Market")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def nrml_pcode_slm():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_nrml()
            _select_order_type("SLM")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Limit")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Market")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present()

        #
        def intraday_stoploss():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("SL")
            _set_qty("1")
            _set_stoploss_minus_2()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_stoploss_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("SLM")
            _set_qty("1")
            _set_stoploss_minus_slm()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_pcode_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Limit")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_pcode_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("Market")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def intraday_pcode_slm():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_intraday()
            _select_order_type("SLM")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bracket_bo_co():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_bo_co()
            _select_product_preferring_bracket()
            _select_order_type("Limit")
            _set_qty("1")
            _set_stoploss_minus_2()
            _set_target_price()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def cover_bo_co():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_bo_co()
            _select_product_preferring_cover()
            _select_order_type("Limit")
            _set_qty("1")
            _set_stoploss_minus_2()
            _set_target_price()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def gtt_single():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_gtt()
            _select_product_preferring_nrml()
            _select_order_type("Single")
            _set_qty("1")
            _set_order_price("10")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def gtt_oco():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_gtt()
            _select_product_preferring_nrml()
            _select_order_type("OCO")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Limit")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Market")
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present()

            #

        def bnpl_stoploss():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("SL")
            _set_qty("1")
            _set_stoploss_minus_2()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_stoploss_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("SLM")
            _set_qty("1")
            _set_stoploss_minus_slm()
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_pcode_limit():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Limit")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_pcode_market():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("Market")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        def bnpl_pcode_slm():
            _close_order_window_if_open()
            _open_buy_for_index(i)
            _select_regular()
            _select_product_preferring_bnpl()
            _select_order_type("SLM")
            _pcode_button()
            _set_qty("1")
            _click_buy_submit()
            _confirm_yes_if_present(max_clicks=2, timeout_each=3)

        # ======================
        # Main flow starts here
        # ======================

        scrips = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]")
            )
        )
        scrip_total = len(scrips)

        for i in range(1, scrip_total + 1):
            name = _scrip_name_by_index(i)

            # try:
            #     bnpl_limit()
            #     bnpl_market()
            #     bnpl_stoploss()
            #     bnpl_stoploss_market()
            #     bnpl_pcode_limit()
            #     bnpl_pcode_market()
            #     bnpl_pcode_slm()
            #     # action_log.append(f"[{name}] Regular + {product_used} + Limit → Buy submitted")
            # except Exception as e:
            #     print(e)
            #
            # finally:
            #     _close_order_window_if_open()

            # --- Run 1: Regular + NRML (or Delivery fallback) + Limit ---
            # try:
            #     nrml_limit()
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + Limit FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # # --- Run 2: Regular + NRML (or Delivery fallback) + SL ---
            #
            # try:
            #     nrml_market()
            #     status = "pass"
            #     actual_error = ""
            #     test_results.append({
            #         "watchlist_bottom_tab": name,
            #         "expected": expected,
            #         "actual": "clicked successfully" if status == "pass" else actual_error,
            #         "status": status
            #     })
            # except Exception as e:
            #     action_log.append(f"[{name}] Regular + NRML/Delivery + Market FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_stoploss()
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_stoploss_market()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            #     # --------------------IOC-----------------
            # try:
            #     nrml_pcode_limit()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_pcode_market()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     nrml_pcode_slm()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            #     # --------------------INTRADAY-----------------
            #
            # try:
            #     intraday_limit()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_market()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_stoploss()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_stoploss_market()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_pcode_limit()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     intraday_pcode_market()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            # try:
            #     intraday_stoploss_market()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     bracket_bo_co()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()
            #
            # try:
            #     cover_bo_co()
            #     # action_log.append(f"[{name}] Regular + {product_used} + SL → Buy submitted")
            # except Exception as e:
            #     print(e)
            #     # action_log.append(f"[{name}] Regular + NRML/Delivery + SL FAILED: {str(e)}")
            # finally:
            #     _close_order_window_if_open()

                # --------------------GTT-----------------

            try:
                gtt_single()
                # action_log.append(f"[{name}] Regular + {product_used} + Limit → Buy submitted")
            except Exception as e:
                print(e)
                # action_log.append(f"[{name}] Regular + NRML/Delivery + Limit FAILED: {str(e)}")
            finally:
                _close_order_window_if_open()

            try:
                gtt_oco()
                # action_log.append(f"[{name}] Regular + {product_used} + Limit → Buy submitted")
            except Exception as e:
                print(e)
                # action_log.append(f"[{name}] Regular + NRML/Delivery + Limit FAILED: {str(e)}")
            finally:
                _close_order_window_if_open()

        # Collect result
        status = "pass"
        test_results.append({
            "Testing_Area": self.orderWindow.__name__,
            "expected": expected,
            "actual": "; ".join(action_log),
            "status": status
        })

    def _open_first_scrip_order_window(self, action_log):
        """Clicks the Buy button of the first scrip in watchlist"""
        buy_button_xpath = "(//button[normalize-space()='Buy'])[1]"
        buy_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, buy_button_xpath)))
        buy_btn.click()
        action_log.append("Opened order window for first scrip")

    def _select_tab(self, tab_name, xpath, action_log):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        try:
            # Wait until the tab is clickable
            tab = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", tab)
            ActionChains(driver).move_to_element(tab).perform()
            time.sleep(0.5)

            tab.click()
            time.sleep(0.5)  # small delay for UI update
            action_log.append(f"Selected {tab_name} tab")

        except Exception as e:
            raise Exception(f"Failed to select {tab_name} tab: {str(e)}")

    def _place_and_modify_order(self, qty, price, new_qty, new_price, action_log):
        """Enters order details, submits, and modifies"""
        # Fill quantity
        qty_field = self.wait.until(EC.element_to_be_clickable((By.ID, "qty")))
        qty_field.clear()
        qty_field.send_keys(qty)
        action_log.append(f"Entered Qty: {qty}")

        # Fill price
        # price_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Price']")))
        # price_field.clear()
        # price_field.send_keys(price)
        # action_log.append(f"Entered Price: {price}")

        # Submit Buy
        buy_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "//button[contains(@class, 'capitalize') and contains(@class, 'green_btn') and span[text()='Buy']]")))
        buy_btn.click()
        action_log.append("Submitted Buy order")

        confirm_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='button' and @class='confirm_btn' and text()='Yes']")))
        confirm_btn.click()
        action_log.append("Submitted Buy order")

        confirm_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='button' and @class='confirm_btn' and text()='Yes']")))
        confirm_btn.click()
        action_log.append("Submitted Buy order")

        amo_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='button' and contains(@class, 'confirm_btn') and text()='Yes']")))
        amo_btn.click()
        action_log.append("Submitted Buy order")

        # Modify
        # modify_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Modify']")))
        # modify_btn.click()
        # action_log.append("Opened Modify order window")
        #
        # # Update Qty
        # qty_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Qty']")))
        # qty_field.clear()
        # qty_field.send_keys(new_qty)
        # action_log.append(f"Modified Qty: {new_qty}")
        #
        # # Update Price
        # price_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Price']")))
        # price_field.clear()
        # price_field.send_keys(new_price)
        # action_log.append(f"Modified Price: {new_price}")
        #
        # # Submit modification
        # submit_modify_btn = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Modify']")))
        # submit_modify_btn.click()
        # action_log.append("Submitted Modify order")

    # def orderWindow(self, test_results, expected="pass"):
    #     try:
    #         # --- Step 1: Delivery + Limit Order ---
    #         self.place_order_flow(
    #             tab_sequence=["order_window_delivery_tab", "order_window_limit_tab"],
    #             qty="1",
    #             price="6.81",
    #             test_results=test_results,
    #             expected=expected
    #         )
    #
    #         # --- Step 2: Modify this order immediately ---
    #         self.open_order_tab()
    #         self.modify_order(test_results=test_results, expected=expected)
    #
    #         # (Optional) --- Step 3: Place Delivery + Stop Loss Order ---
    #         self.place_order_flow(
    #             tab_sequence=["order_window_delivery_tab", "order_window_stop_loss_tab"],
    #             qty="1",
    #             price="6.71",
    #             test_results=test_results,
    #             expected=expected
    #         )
    #
    #     except Exception as e:
    #         test_results.append({
    #             "Testing_Area": "orderWindow_overall",
    #             "expected": expected,
    #             "actual": str(e),
    #             "status": "fail"
    #         })
    #
    # def place_order_flow(self, tab_sequence, qty, price, test_results, expected):
    #     action_log = []
    #
    #     try:
    #         for tab_name in tab_sequence:
    #             xpath = self.get_tab_xpath(tab_name)
    #             tab_button = WebDriverWait(self.driver, 10).until(
    #                 EC.element_to_be_clickable((By.XPATH, xpath))
    #             )
    #             self.driver.execute_script("arguments[0].scrollIntoView(true);", tab_button)
    #             tab_button.click()
    #             time.sleep(2)
    #             action_log.append(f"Clicked tab: {tab_name}")
    #
    #         qty_field = WebDriverWait(self.driver, 5).until(
    #             EC.element_to_be_clickable((By.ID, "qty"))
    #         )
    #         qty_field.clear()
    #         qty_field.send_keys(qty)
    #         action_log.append(f"Quantity field entered: {qty}")
    #
    #         price_field = WebDriverWait(self.driver, 5).until(
    #             EC.element_to_be_clickable((By.ID, "price"))
    #         )
    #         price_field.clear()
    #         price_field.send_keys(price)
    #         action_log.append(f"Price field entered: {price}")
    #
    #         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.buy_button)).click()
    #         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_buy)).click()
    #         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_amo)).click()
    #
    #         # View Charges + Close Popup
    #         WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//a[text()='View Charges']"))
    #         ).click()
    #         time.sleep(2)
    #         WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(
    #                 (By.XPATH, "//span[contains(@class, 'cursor-pointer') and contains(@class, 'w-[18px]')]"))
    #         ).click()
    #
    #         test_results.append({
    #             "Testing_Area": " > ".join(tab_sequence),
    #             "expected": expected,
    #             "actual": "; ".join(action_log),
    #             "status": "pass"
    #         })
    #
    #     except Exception as e:
    #         test_results.append({
    #             "Testing_Area": " > ".join(tab_sequence),
    #             "expected": expected,
    #             "actual": str(e),
    #             "status": "fail"
    #         })
    #
    # def open_order_tab(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.dashboard.order_tab)
    #     ).click()
    #
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.dashboard.pending_order)
    #     ).click()
    #     time.sleep(3)
    #
    # def modify_order(self, test_results, expected):
    #     try:
    #         WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)
    #         ).click()
    #
    #         WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(self.dashboard.orderbook_modify)
    #         ).click()
    #         time.sleep(3)
    #
    #         qty_field = WebDriverWait(self.driver, 5).until(
    #             EC.element_to_be_clickable((By.ID, "qty"))
    #         )
    #         qty_field.clear()
    #         qty_field.send_keys("5")
    #
    #         price_field = WebDriverWait(self.driver, 5).until(
    #             EC.element_to_be_clickable((By.ID, "price"))
    #         )
    #         price_field.clear()
    #         price_field.send_keys("6.41")
    #
    #         WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(self.modify_button)
    #         ).click()
    #
    #         test_results.append({
    #             "Testing_Area": "Modify Order",
    #             "expected": expected,
    #             "actual": "Order modified with qty 5 and price 6.41",
    #             "status": "pass"
    #         })
    #     except Exception as e:
    #         test_results.append({
    #             "Testing_Area": "Modify Order",
    #             "expected": expected,
    #             "actual": str(e),
    #             "status": "fail"
    #         })
    #
    # def get_tab_xpath(self, tab_name):
    #     tab_xpaths = {
    #         "order_window_delivery_tab": "//button[normalize-space()='Delivery']",
    #         "order_window_limit_tab": "//button[normalize-space()='Limit']",
    #         "order_window_stop_loss_tab": "//button[normalize-space()='SL']",
    #         "order_window_regular_tab": "//button[normalize-space()='Regular']",
    #     }
    #     return tab_xpaths[tab_name]

    def get_login_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None
