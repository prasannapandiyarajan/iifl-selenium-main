import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("search_scrip,expected", [
    ("ABB-EQ", "pass"),
    ("ABB", "pass"),

])
def test_watchlist_scenarios(browserInstance, search_scrip, expected):
    driver = browserInstance
    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)

    try:
        # STEP 1: Enter the scrip in the search field
        search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='watch_search_inp']")))
        search_input.clear()
        search_input.send_keys(search_scrip)
        time.sleep(2)  # Allow dropdown to populate

        # STEP 2: Get all matching scrip entries
        result_items = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@id,'_search_scrip_name')]")
        ))

        found = False
        for scrip_element in result_items:
            scrip_text = scrip_element.text.strip()

            if scrip_text == search_scrip:
                # Scroll to view and hover
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", scrip_element)
                actions.move_to_element(scrip_element).pause(0.5).perform()

                try:
                    # Find the Add button related to this scrip
                    add_button = scrip_element.find_element(By.XPATH,
                                                            "./ancestor::li//button[contains(@class, 'bg-[#e8f4ff]')]")
                    driver.execute_script("arguments[0].click();", add_button)
                    print(f"✅ Successfully added scrip: {search_scrip}")
                    found = True
                    break
                except Exception as e:
                    print(f"⚠️ Add button not found or not clickable: {e}")

        if not found:
            raise Exception(f"❌ Could not find or add scrip: {search_scrip}")

    except Exception as e:
        print(f"❌ Error in test_watchlist_scenarios: {e}")
        assert expected != "pass", f"Test failed for scrip: {search_scrip}"

        def orderWindow(self, test_results, expected="pass"):
            try:
                driver = self.driver
                wait = WebDriverWait(driver, 15)
                action_log = []

                # STEP 0: Find first scrip and click Buy
                try:
                    print("\n=== Locating First Available Scrip ===")
                    scrip = wait.until(EC.presence_of_element_located((
                        By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]"
                    )))
                    driver.execute_script("arguments[0].scrollIntoView(true);", scrip)
                    ActionChains(driver).move_to_element(scrip).perform()
                    time.sleep(1)

                    print("=== Clicking Buy Button ===")
                    buy_button = wait.until(EC.element_to_be_clickable((
                        By.XPATH, ".//button[normalize-space()='B']"
                    )))
                    buy_button.click()
                    action_log.append("Clicked Buy button on first available scrip")
                    time.sleep(8)

                    self._select_tab("Regular", '//nav[@id="order_tabs"]//button[text()="Regular"]', action_log)
                    self._select_tab("Delivery", "//button[contains(normalize-space(), 'Delivery')]", action_log)
                    self._select_tab("Limit", "//button[contains(normalize-space(), 'Limit')]", action_log)

                    # Fill quantity
                    qty_field = wait.until(EC.element_to_be_clickable((By.ID, "qty")))
                    qty_field.clear()
                    qty_field.send_keys("1")

                    # Click Buy in order form
                    form_buy_btn = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//button[contains(@class, 'green_btn') and .//span[normalize-space()='Buy']]"
                    )))
                    form_buy_btn.click()
                    action_log.append("Submitted Buy order")

                    # Confirm
                    confirm_btn = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
                    )))
                    confirm_btn.click()
                    action_log.append("Confirmed Buy order")

                    time.sleep(2)

                    amo_btn = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
                    )))
                    amo_btn.click()
                    time.sleep(2)

                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.dashboard.order_tab)
                    ).click()

                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.dashboard.pending_order)
                    ).click()

                    time.sleep(5)

                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)
                    ).click()

                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.dashboard.orderbook_modify)
                    ).click()

                    time.sleep(5)

                    qty_input = driver.find_element(By.XPATH, "//input[@id='qty']")
                    qty_input.click()  # focus input

                    for _ in range(5):  # press down arrow 4 times
                        time.sleep(1)
                        qty_input.send_keys(Keys.ARROW_UP)

                    price_input = driver.find_element(By.XPATH, "//input[@id='price']")
                    price_input.click()  # focus input

                    for _ in range(20):  # press down arrow 4 times
                        time.sleep(1)
                        price_input.send_keys(Keys.ARROW_DOWN)

                    time.sleep(2)

                    # ✅ Click Modify button
                    modify_button = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((
                            By.XPATH, "//button[.//span[normalize-space()='Modify']]"
                        ))
                    )

                    # Scroll into view
                    driver.execute_script("arguments[0].scrollIntoView(true);", modify_button)

                    # Try normal click, fallback to JS click
                    try:
                        modify_button.click()
                        action_log.append("Clicked Modify button")
                        time.sleep(15)
                    except:
                        driver.execute_script("arguments[0].click();", modify_button)
                        action_log.append("Clicked Modify button using JS")

                    print("✅ Modify flow executed successfully")
                except Exception as e:
                    raise Exception(f"Failed to open order window: {str(e)}")

                # STEP 1: DELIVERY + LIMIT

                # STEP 2: Open order window again for SL
                # self._reopen_first_scrip_order_window()
                #
                # # STEP 3: DELIVERY + SL
                # self._select_tab("Delivery", "//button[normalize-space()='Delivery']", action_log)
                # self._select_tab("SL", "//button[normalize-space()='SL']", action_log)
                # # self._place_and_modify_order(qty="1", new_qty="3",action_log=action_log)

                status = "pass"
                test_results.append({
                    "Testing_Area": self.orderWindow.__name__,
                    "expected": expected,
                    "actual": "; ".join(action_log),
                    "status": status
                })

            except Exception as e:
                status = "fail"
                test_results.append({
                    "Testing_Area": self.orderWindow.__name__,
                    "expected": expected,
                    "actual": str(e),
                    "status": status
                })


# def orderWindow(self, test_results, expected="pass"):
#     try:
#         driver = self.driver
#         wait = WebDriverWait(driver, 15)
#         action_log = []
#
#         # STEP 0: Find all scrips in watchlist
#         print("\n=== Locating All Available Scrips ===")
#         scrips = wait.until(EC.presence_of_all_elements_located((
#             By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]"
#         )))
#
#         print(f"✅ Found {len(scrips)} scrips in watchlist")
#
#         # Loop through first 4 scrips (or all if fewer)
#         for idx, scrip in enumerate(scrips[:4], start=1):
#             try:
#                 print(f"\n=== Processing Scrip {idx} ===")
#                 driver.execute_script("arguments[0].scrollIntoView(true);", scrip)
#                 ActionChains(driver).move_to_element(scrip).perform()
#                 time.sleep(1)
#
#                 # --- Click Buy Button ---
#                 print("=== Clicking Buy Button ===")
#                 buy_button = scrip.find_element(By.XPATH, ".//button[normalize-space()='B']")
#                 driver.execute_script("arguments[0].click();", buy_button)
#                 action_log.append(f"Clicked Buy button on scrip {idx}")
#                 time.sleep(8)
#
#                 # --- Select Tabs ---
#                 self._select_tab("Regular", '//nav[@id="order_tabs"]//button[text()="Regular"]', action_log)
#                 self._select_tab("Delivery", "//button[contains(normalize-space(), 'Delivery')]", action_log)
#                 self._select_tab("Limit", "//button[contains(normalize-space(), 'Limit')]", action_log)
#
#                 # --- Fill Quantity ---
#                 qty_field = wait.until(EC.element_to_be_clickable((By.ID, "qty")))
#                 qty_field.clear()
#                 qty_field.send_keys("1")
#
#                 # --- Place Buy Order ---
#                 form_buy_btn = wait.until(EC.element_to_be_clickable((
#                     By.XPATH, "//button[contains(@class, 'green_btn') and .//span[normalize-space()='Buy']]"
#                 )))
#                 form_buy_btn.click()
#                 action_log.append(f"Submitted Buy order for scrip {idx}")
#
#                 # --- Confirm ---
#                 confirm_btn = wait.until(EC.element_to_be_clickable((
#                     By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
#                 )))
#                 confirm_btn.click()
#                 action_log.append(f"Confirmed Buy order for scrip {idx}")
#                 time.sleep(2)
#
#                 # --- AMO Confirmation ---
#                 try:
#                     amo_btn = wait.until(EC.element_to_be_clickable((
#                         By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
#                     )))
#                     amo_btn.click()
#                     time.sleep(2)
#                 except:
#                     print("⚠️ AMO confirmation not found, continuing...")
#
#                 # --- Go to Orders and Modify ---
#                 WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable(self.dashboard.order_tab)
#                 ).click()
#
#                 WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable(self.dashboard.pending_order)
#                 ).click()
#
#                 time.sleep(5)
#
#                 WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)
#                 ).click()
#
#                 WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable(self.dashboard.orderbook_modify)
#                 ).click()
#
#                 time.sleep(5)
#
#                 # --- Modify Qty ---
#                 qty_input = driver.find_element(By.XPATH, "//input[@id='qty']")
#                 qty_input.click()
#                 for _ in range(5):
#                     time.sleep(1)
#                     qty_input.send_keys(Keys.ARROW_UP)
#
#                 # --- Modify Price ---
#                 price_input = driver.find_element(By.XPATH, "//input[@id='price']")
#                 price_input.click()
#                 for _ in range(20):
#                     time.sleep(1)
#                     price_input.send_keys(Keys.ARROW_DOWN)
#
#                 # --- Click Modify ---
#                 modify_button = WebDriverWait(driver, 15).until(
#                     EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Modify']]"))
#                 )
#                 driver.execute_script("arguments[0].scrollIntoView(true);", modify_button)
#                 try:
#                     modify_button.click()
#                 except:
#                     driver.execute_script("arguments[0].click();", modify_button)
#
#                 action_log.append(f"Modified order for scrip {idx}")
#                 print(f"✅ Modify flow executed successfully for scrip {idx}")
#                 time.sleep(5)
#
#             except Exception as e:
#                 action_log.append(f"❌ Failed for scrip {idx}: {str(e)}")
#                 print(f"❌ Failed on scrip {idx}: {str(e)}")
#                 continue
#
#         status = "pass"
#         test_results.append({
#             "Testing_Area": self.orderWindow.__name__,
#             "expected": expected,
#             "actual": "; ".join(action_log),
#             "status": status
#         })
#
#     except Exception as e:
#         status = "fail"
#         test_results.append({
#             "Testing_Area": self.orderWindow.__name__,
#             "expected": expected,
#             "actual": str(e),
#             "status": status
#         })
#
#
#  def orderWindowSell(self, test_results, expected="pass"):
#         try:
#             driver = self.driver
#             wait = WebDriverWait(driver, 15)
#             action_log = []
#
#             # STEP 0: Find first scrip and click Sell
#             print("\n=== Locating First Available Scrip for Sell ===")
#             scrip = wait.until(EC.presence_of_element_located((
#                 By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]"
#             )))
#             driver.execute_script("arguments[0].scrollIntoView(true);", scrip)
#             ActionChains(driver).move_to_element(scrip).perform()
#             time.sleep(1)
#
#             print("=== Clicking Sell Button ===")
#             sell_button = wait.until(EC.element_to_be_clickable((
#                 By.XPATH, ".//button[normalize-space()='S']"
#             )))
#             sell_button.click()
#             action_log.append("Clicked Sell button on first available scrip")
#             time.sleep(8)
#
#             # Select order type tabs
#
#             try:
#                 self._select_tab("Regular", '//nav[@id="order_tabs"]//button[text()="Regular"]', action_log)
#                 self._select_tab("Delivery", "//button[contains(normalize-space(), 'Delivery')]", action_log)
#                 self._select_tab("Limit", "//button[contains(normalize-space(), 'Limit')]", action_log)
#             except Exception as e:
#                 print(e)
#
#             # Fill quantity
#             qty_field = wait.until(EC.element_to_be_clickable((By.ID, "qty")))
#             qty_field.clear()
#             qty_field.send_keys("150")
#
#             # Click Sell in order form
#             form_sell_btn = wait.until(EC.element_to_be_clickable((
#                 By.XPATH, "//button[contains(@class,'red_btn')]//*[normalize-space()='Sell']"
#             )))
#             driver.execute_script("arguments[0].scrollIntoView(true);", form_sell_btn)
#             driver.execute_script("arguments[0].click();", form_sell_btn)
#             action_log.append("Submitted Sell order")
#
#             # Confirm order
#             confirm_btn = wait.until(EC.element_to_be_clickable((
#                 By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
#             )))
#             confirm_btn.click()
#             action_log.append("Confirmed Sell order")
#
#             time.sleep(2)
#
#             # Handle AMO confirm (if present)
#             amo_btn = wait.until(EC.element_to_be_clickable((
#                 By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
#             )))
#             amo_btn.click()
#             time.sleep(2)
#
#             # Navigate to order tab
#             WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable(self.dashboard.order_tab)
#             ).click()
#
#             WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable(self.dashboard.pending_order)
#             ).click()
#
#             time.sleep(5)
#
#             # Select order in orderbook
#             WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)
#             ).click()
#
#             WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable(self.dashboard.orderbook_modify)
#             ).click()
#
#             time.sleep(5)
#
#             # Modify qty
#             qty_input = driver.find_element(By.XPATH, "//input[@id='qty']")
#             qty_input.click()
#             for _ in range(2):  # increase quantity
#                 qty_input.send_keys(Keys.ARROW_UP)
#                 time.sleep(0.5)
#
#             # Modify price
#             price_input = driver.find_element(By.XPATH, "//input[@id='price']")
#             price_input.click()
#             for _ in range(4):  # decrease price
#                 price_input.send_keys(Keys.ARROW_DOWN)
#                 time.sleep(0.5)
#
#             time.sleep(2)
#
#             # ✅ Click Modify button
#             modify_button = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((
#                     By.XPATH, "//button[.//span[normalize-space()='Modify']]"
#                 ))
#             )
#
#             driver.execute_script("arguments[0].scrollIntoView(true);", modify_button)
#
#             try:
#                 modify_button.click()
#                 action_log.append("Clicked Modify button for Sell order")
#                 time.sleep(10)
#             except:
#                 driver.execute_script("arguments[0].click();", modify_button)
#                 action_log.append("Clicked Modify button using JS for Sell order")
#
#             print("✅ Sell + Modify flow executed successfully")
#
#             status = "pass"
#             test_results.append({
#                 "Testing_Area": self.orderWindowSell.__name__,
#                 "expected": expected,
#                 "actual": "; ".join(action_log),
#                 "status": status
#             })
#
#         except Exception as e:
#             status = "fail"
#             test_results.append({
#                 "Testing_Area": self.orderWindowSell.__name__,
#                 "expected": expected,
#                 "actual": str(e),
#                 "status": status
#             })



    def orderWindow(self, test_results, expected="pass"):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 15)
            action_log = []

            # STEP 0: Find all scrips in watchlist
            print("\n=== Locating All Available Scrips ===")
            scrips = wait.until(EC.presence_of_all_elements_located((
                By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]"
            )))

            print(f"✅ Found {len(scrips)} scrips in watchlist")

            # Loop through first 4 scrips (or all if fewer)
            for idx, scrip in enumerate(scrips, start=1):
                try:
                    print(f"\n=== Processing Scrip {idx} ===")
                    driver.execute_script("arguments[0].scrollIntoView(true);", scrip)
                    ActionChains(driver).move_to_element(scrip).perform()
                    time.sleep(1)

                    # --- Click Buy Button ---
                    print("=== Clicking Buy Button ===")
                    buy_button = scrip.find_element(By.XPATH, ".//button[normalize-space()='B']")
                    driver.execute_script("arguments[0].click();", buy_button)
                    action_log.append(f"Clicked Buy button on scrip {idx}")
                    time.sleep(1)

                    # --- Select Tabs ---
                    try:
                        self._select_tab("Regular", '//nav[@id="order_tabs"]//button[text()="Regular"]', action_log)
                        self._select_tab("Delivery", "//button[contains(normalize-space(), 'Delivery')]", action_log)
                        self._select_tab("Limit", "//button[contains(normalize-space(), 'Limit')]", action_log)
                    except Exception as e:
                        print()
                    # --- Fill Quantity ---
                    qty_field = wait.until(EC.element_to_be_clickable((By.ID, "qty")))
                    qty_field.clear()
                    qty_field.click()
                    for _ in range(5):
                        time.sleep(1)
                        qty_field.send_keys(Keys.ARROW_UP)

                    # --- Place Buy Order ---
                    form_buy_btn = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//button[contains(@class, 'green_btn') and .//span[normalize-space()='Buy']]"
                    )))
                    form_buy_btn.click()
                    action_log.append(f"Submitted Buy order for scrip {idx}")

                    # --- Confirm ---
                    confirm_btn = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
                    )))
                    confirm_btn.click()
                    action_log.append(f"Confirmed Buy order for scrip {idx}")
                    time.sleep(2)

                    # --- AMO Confirmation ---
                    try:
                        amo_btn = wait.until(EC.element_to_be_clickable((
                            By.XPATH, "//button[@type='button' and contains(@class,'confirm_btn') and text()='Yes']"
                        )))
                        amo_btn.click()
                        time.sleep(2)

                    except:

                        print("jjj")

                    # --- Go to Orders and Modify ---
                    # WebDriverWait(driver, 10).until(
                    #     EC.element_to_be_clickable(self.dashboard.order_tab)
                    # ).click()
                    #
                    # WebDriverWait(driver, 10).until(
                    #     EC.element_to_be_clickable(self.dashboard.pending_order)
                    # ).click()
                    #
                    # time.sleep(5)
                    #
                    # WebDriverWait(driver, 10).until(
                    #     EC.element_to_be_clickable(self.dashboard.checkbox_orderbook)
                    # ).click()
                    #
                    # WebDriverWait(driver, 10).until(
                    #     EC.element_to_be_clickable(self.dashboard.orderbook_modify)
                    # ).click()
                    #
                    # time.sleep(5)
                    #
                    # # --- Modify Qty ---
                    # qty_input = driver.find_element(By.XPATH, "//input[@id='qty']")
                    # qty_input.click()
                    # for _ in range(5):
                    #     time.sleep(1)
                    #     qty_input.send_keys(Keys.ARROW_UP)
                    #
                    # # --- Modify Price ---
                    # price_input = driver.find_element(By.XPATH, "//input[@id='price']")
                    # price_input.click()
                    # for _ in range(20):
                    #     time.sleep(1)
                    #     price_input.send_keys(Keys.ARROW_DOWN)
                    #
                    # # --- Click Modify ---
                    # modify_button = WebDriverWait(driver, 15).until(
                    #     EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Modify']]"))
                    # )
                    # driver.execute_script("arguments[0].scrollIntoView(true);", modify_button)
                    # try:
                    #     modify_button.click()
                    # except:
                    #     driver.execute_script("arguments[0].click();", modify_button)
                    #
                    # action_log.append(f"Modified order for scrip {idx}")
                    # print(f"✅ Modify flow executed successfully for scrip {idx}")
                    # time.sleep(5)

                except Exception as e:
                    action_log.append(f"[FAIL] Failed for scrip {idx}: {str(e)}")
                    print(f"Failed on scrip {idx}: {str(e)}")
                    continue

            status = "pass"
            test_results.append({
                "Testing_Area": self.orderWindow.__name__,
                "expected": expected,
                "actual": "; ".join(action_log),
                "status": status
            })

        except Exception as e:
            status = "fail"
            test_results.append({
                "Testing_Area": self.orderWindow.__name__,
                "expected": expected,
                "actual": str(e),
                "status": status
            })