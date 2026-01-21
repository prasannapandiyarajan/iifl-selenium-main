import csv
# pytest -m smoke   // Tagging
# pytest -n 10 //pytest-xdist plugin you need to run in parallel

# pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html

import os
import sys
import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSelectorException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pageObjects.login import LoginData
from pageObjects.otp import otpPage
from pageObjects.funds import FundsPage
from pageObjects.explore import ExplorePage
from pageObjects.watchlist import WatchList
from pageObjects.orders import OrderBook
from pageObjects.order_window import orderWindowPage
from pageObjects.dashboard import dashBoardPage
from pageObjects.predefined_watchlist import predefinedWatchList

test_results = []


# def reset_application(driver):
#     """Safe navigation to home page, reload if session is alive."""
#     try:
#         driver.get("https://iifl.codifi.in/web/#")
#     except Exception as e:
#         print(f"Session broken. Error: {e}")
#         pytest.exit("Browser session is closed or crashed. Please rerun tests.")


# ===========================
# Test: Login Scenarios
# ===========================
# @pytest.mark.parametrize("username,password,expected", [
#     ("TEST109", "Test@9191", "fail"),
#     ("TEST110", "Test@505", "fail"),
#     ("TEST109", "Test@505", "pass"),
# ])
# def test_login_scenarios(browserInstance, username, password, expected):
#     driver = browserInstance
#     # reset_application(driver)
#
#     loginPage = LoginData(driver)
#     loginPage.login(username, password)
#
#     actual_error = loginPage.get_login_error()
#     status = "pass" if expected == "pass" and not actual_error else "fail"
#
#     test_results.append({
#         "username": username,
#         "password": password,
#         "expected": expected,
#         "actual": "error shown" if actual_error else "login success",
#         "status": status
#     })
#     print(test_results)
#     assert status == expected


# ===========================
# Test: Forgot Password
# ===========================

# @pytest.mark.parametrize("username,pannumber,expected", [
#     ("TEST109", "BTYPA1822P", "fail"),
#     ("TEST110", "BTYPA1822L", "fail"),
#     ("TEST109", "BTYPA1822L", "pass"),
# ])
# def test_login_forgotpassword(browserInstance, username, pannumber, expected):
#     driver = browserInstance
#     print(f"\nRunning test for: {username} | {pannumber} | expected={expected}")
#
#     loginPage = LoginData(driver)
#     loginPage.forgot_password(username, pannumber)
#
#     actual_error = loginPage.get_login_error()
#     status = "pass" if expected == "pass" and not actual_error else "fail"
#
#     result = {
#         "username": username,
#         "pannumber": pannumber,
#         "expected": expected,
#         "actual": "error shown" if actual_error else "forgot password success",
#         "status": status
#     }
#
#     test_results.append(result)
#     print(result)
#     assert status == expected, f"Expected {expected} but got {status}"


# @pytest.mark.parametrize("username,pannumber,expected", [
#     ("TEST109", "BTYPA1822P", "fail"),
#     ("TEST110", "BTYPA1822L", "fail"),
#     ("TEST109", "BTYPA1822L", "pass"),
# ])
# def test_login_forgotpassword(browserInstance, username, pannumber, expected):
#     driver = browserInstance
#
#     try:
#         print(f"\n▶ Running test for: {username} | {pannumber} | expected={expected}")
#
#         loginPage = LoginData(driver)
#
#         # Optional: reset page state if needed
#         driver.get("https://sandboxmarkets.iiflcapital.com/")
#
#         # Handle captcha/TFLite issues gracefully
#         try:
#             loginPage.forgot_password(username, pannumber)
#         except RuntimeError as e:
#             if "delegate" in str(e) or "dynamic-sized tensors" in str(e):
#                 raise AssertionError(f"TFLite crash for {username} - Tensor size mismatch") from e
#             else:
#                 raise
#
#         # Validation logic
#         actual_error = loginPage.get_login_error()
#         status = "pass" if expected == "pass" and not actual_error else "fail"
#
#         # Collect result
#         result = {
#             "username": username,
#             "pannumber": pannumber,
#             "expected": expected,
#             "actual": "error shown" if actual_error else "forgot password success",
#             "status": status
#         }
#
#         print("✅ Test Result:", result)
#         test_results.append(result)
#         assert status == expected, f"Expected {expected}, but got {status}"
#
#     except Exception as e:
#         # Save screenshot on failure
#         file_path = os.path.join(
#             "reports", f"test_login_forgotpassword_{username}_{pannumber}.png"
#         )
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         driver.save_screenshot(file_path)
#         print(f"❌ Error: Test failed for {username}. Screenshot saved at: {file_path}")
#         raise


# ===========================
# Test: OTP Validation
# ===========================

# @pytest.mark.parametrize("otpvalue,expected", [
#     ("123456", "pass"),
# ])
# def test_login_otp(browserInstance, otpvalue, expected):
#     driver = browserInstance
#
#     # reset_application(driver)
#
#     otppage = otpPage(driver)
#     try:
#         otppage.enter_input(str(otpvalue))
#     except RuntimeError as e:
#         if "delegate" in str(e) or "dynamic-sized tensors" in str(e):
#             raise AssertionError(f"TFLite crash for {otpvalue} - Tensor size mismatch") from e
#         else:
#             raise
#
#     actual_error = otppage.get_login_error()
#
#     if actual_error:
#         actual_result = "fail"
#         actual_message = "error shown"
#     else:
#         actual_result = "pass"
#         actual_message = "OTP validated successfully"
#
#     test_results.append({
#         "otp": otpvalue,
#         "expected": expected,
#         "actual": actual_message,
#         "status": "pass" if actual_result == expected else "fail"
#     })
#
#     print(test_results)
#     assert actual_result == expected
#
#
# @pytest.mark.parametrize("newpassword,conformpassword,expected", [
#     ("Test@005", "Test@935", "fail"),
#     ("Test@935", "Test@005", "fail"),
#     ("Test@005", "Test@005", "pass"),
#
# ])
# def test_password_reset(browserInstance, newpassword, conformpassword, expected):
#     driver = browserInstance
#
#     try:
#         print(f"\n▶ Running test for: {newpassword} | {conformpassword} | expected={expected}")
#
#         setPasswordpage = passwordPage(driver)
#
#         # Handle captcha/TFLite issues gracefully
#         try:
#             setPasswordpage.password_field(newpassword, conformpassword)
#         except RuntimeError as e:
#             if "delegate" in str(e) or "dynamic-sized tensors" in str(e):
#                 raise AssertionError(f"TFLite crash for {newpassword} - Tensor size mismatch") from e
#             else:
#                 raise
#
#         # Validation logic
#         actual_error = setPasswordpage.get_login_error()
#         status = "pass" if expected == "pass" and not actual_error else "fail"
#
#         # Collect result
#         result = {
#             "password": newpassword,
#             "conformpassword": conformpassword,
#             "expected": expected,
#             "actual": "error shown" if actual_error else "forgot password success",
#             "status": status
#         }
#
#         print("✅ Test Result:", result)
#         test_results.append(result)
#
#         assert status == expected, f"Expected {expected}, but got {status}"
#
#     except Exception as e:
#         # Save screenshot on failure
#         file_path = os.path.join(
#             "reports", f"test_login_forgotpassword_{newpassword}_{conformpassword}.png"
#         )
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         driver.save_screenshot(file_path)
#         print(f"❌ Error: Test failed for {newpassword}. Screenshot saved at: {file_path}")
#         raise


@pytest.mark.parametrize("username,password,expected", [
    # ("TEST109", "Admin@123", "pass"),
    # ("TEST110", "Test@005", "fail"),
    ("11882058", "Admin@11", "pass"),
])
def test_login_scenarios(browserInstance, username, password, expected):
    driver = browserInstance
    loginPage = LoginData(driver)

    try:
        loginPage.login(username, password)
    except Exception as e:
        print(f"❌ Login function failed: {e}")
        driver.save_screenshot(f"reports/login_error_{username}.png")
        raise

    actual_error = loginPage.get_login_error()
    print(f"Actual error message: {actual_error}")

    status = "fail" if actual_error else "pass"

    test_results.append({
        "username": username,
        "password": password,
        "expected": expected,
        "actual": "login success" if not actual_error else f"error: {actual_error}",
        "status": status
    })

    driver.save_screenshot(f"reports/login_{username}_{status}.png")
    assert status == expected, f"❌ Test Failed: expected {expected}, got {status}"


@pytest.mark.parametrize("otpvalue,expected", [
    ("123456", "pass"),
])
def test_login_otp(browserInstance, otpvalue, expected):
    driver = browserInstance

    # reset_application(driver)

    otppage = otpPage(driver)
    try:
        otppage.enter_input(str(otpvalue))
    except RuntimeError as e:
        if "delegate" in str(e) or "dynamic-sized tensors" in str(e):
            raise AssertionError(f"TFLite crash for {otpvalue} - Tensor size mismatch") from e
        else:
            raise

    actual_error = otppage.get_login_error()

    if actual_error:
        actual_result = "fail"
        actual_message = "error shown"
    else:
        actual_result = "pass"
        actual_message = "OTP validated successfully"

    test_results.append({
        "otp": otpvalue,
        "expected": expected,
        "actual": actual_message,
        "status": "pass" if actual_result == expected else "fail"
    })

    print(test_results)
    assert actual_result == expected


# @pytest.mark.parametrize("username,pannumber,expected", [
#     ("TEST109", "BTYPA1822L", "pass"),
# ])
# def test_unblock_user(browserInstance, username, pannumber, expected):
#     driver = browserInstance
#
#     try:
#         print(f"\n▶ Running test for: {username} | {pannumber} | expected={expected}")
#
#         loginPage = LoginData(driver)
#
#         # Optional: reset page state if needed
#         driver.get("https://sandboxmarkets.iiflcapital.com/")
#
#         # Handle captcha/TFLite issues gracefully
#         try:
#             loginPage.forgot_password(username, pannumber)
#         except RuntimeError as e:
#             if "delegate" in str(e) or "dynamic-sized tensors" in str(e):
#                 raise AssertionError(f"TFLite crash for {username} - Tensor size mismatch") from e
#             else:
#                 raise
#
#         # Validation logic
#         actual_error = loginPage.get_login_error()
#         status = "pass" if expected == "pass" and not actual_error else "fail"
#
#         # Collect result
#         result = {
#             "username": username,
#             "pannumber": pannumber,
#             "expected": expected,
#             "actual": "error shown" if actual_error else "forgot password success",
#             "status": status
#         }
#
#         print("✅ Test Result:", result)
#         test_results.append(result)
#         assert status == expected, f"Expected {expected}, but got {status}"
#
#     except Exception as e:
#         # Save screenshot on failure
#         file_path = os.path.join(
#             "reports", f"test_login_forgotpassword_{username}_{pannumber}.png"
#         )
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         driver.save_screenshot(file_path)
#         print(f"❌ Error: Test failed for {username}. Screenshot saved at: {file_path}")
#         raise

@pytest.mark.parametrize("search_scrip,expected", [
    # ("CDSL 30 SEP 2025 FUT", "pass"),
    # ("MCX 30 SEP 2025 FUT", "pass"),
    ("ACC-EQ", "pass"),
    # ("BANKNIFTY 30 SEP 2025 FUT", "pass"),
    # ("MIDCPNIFTY 30 SEP 2025 FUT", "pass"),
    # ("FINNIFTY 30 SEP 2025 FUT", "pass"),
    # ("NIFTY 30 SEP 2025 FUT", "pass"),
    # ("CRUDEOILM 20 OCT 2025 FUT","pass"),
    # ("BANKNIFTY 30 SEP 2025 31000 CE", "pass"),
    # ("NIFTY 50", "pass"),
    ("SENSEX", "pass"),

])
def test_watchlist_scenarios(browserInstance, search_scrip, expected):
    driver = browserInstance
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    WatchListData = LoginData(driver)

    search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='watch_search_inp']")))
    search_input.clear()
    search_input.send_keys(search_scrip)

    time.sleep(1.5)  # Let suggestions load

    scrip_xpath = f"//div[contains(@id,'_search_scrip_name') and normalize-space(text())='{search_scrip}']"
    scrip_element = wait.until(EC.presence_of_element_located((By.XPATH, scrip_xpath)))
    webdriver.ActionChains(driver).move_to_element(scrip_element).perform()
    time.sleep(1)

    # Add button inside the row
    # add_button_xpath = f"{scrip_xpath}/ancestor::li//button[contains(@class, 'e8f4ff')]"
    add_button_xpath = f"{scrip_xpath}/ancestor::li//button[contains(@id,'_search_scrip_add')]"
    # add_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_button_xpath)))
    # driver.execute_script("arguments[0].click();", add_button)

    # try:
    # WatchListData.search_data(search_scrip)
    # search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='watch_search_inp']")))
    # search_input.clear()
    # search_input.send_keys(search_scrip)
    #
    # time.sleep(1.5)  # Let suggestions load

    #     scrip_xpath = f"//div[contains(@id,'_search_scrip_name') and normalize-space(text())='{search_scrip}']"
    #     scrip_element = wait.until(EC.presence_of_element_located((By.XPATH, scrip_xpath)))
    #     webdriver.ActionChains(driver).move_to_element(scrip_element).perform()
    #
    #     time.sleep(1)
    #
    #     add_button_xpath = f"{scrip_xpath}/ancestor::li//button[contains(@class, 'e8f4ff')]"
    #     add_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_button_xpath)))
    #     driver.execute_script("arguments[0].click();", add_button)
    #
    # except Exception as e:
    #     print(f"❌ Login function failed: {e}")
    #     driver.save_screenshot(f"reports/login_error_{search_scrip}.png")
    #     raise
    try:
        # Try clicking add button
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_button_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        driver.execute_script("arguments[0].click();", add_button)
        print(f"✅ Add button clicked for {search_scrip}")
    except:
        # If add button fails, click the row
        driver.execute_script("arguments[0].scrollIntoView(true);", scrip_element)
        driver.execute_script("arguments[0].click();", scrip_element)

    # actual_error = WatchListData.get_login_error()
    # print(f"Actual error message: {actual_error}")
    #
    # status = "fail" if actual_error else "pass"
    #
    # test_results.append({
    #     "scrip_name": search_scrip,
    #     "expected": expected,
    #     "actual": "scrip added success" if not actual_error else f"error: {actual_error}",
    #     "status": status
    # })
    #
    # driver.save_screenshot(f"reports/login_{search_scrip}_{status}.png")
    # assert status == expected, f"❌ Test Failed: expected {expected}, got {status}"
    #


# def test_watchlist(browserInstance):
#     driver = browserInstance
#     wait = WebDriverWait(driver, 20)
#     predefined_watchlist = WatchList(driver)
#     expected = "pass"
#
#     try:
#         time.sleep(2)
#         predefined_watchlist.watchlist_setting(test_results, expected)
#         time.sleep(2)
#         # watchlist_tabs_2.nifty_tab()
#         # time.sleep(2)
#
#         actual_error = ""  # No error if everything works
#
#     # except InvalidSelectorException as e:
#     #     actual_error = f"❌ Syntax error in XPath: {str(e)}"
#
#     except (NoSuchElementException, TimeoutException) as e:
#         actual_error = f"Element not found: {str(e)}"
#
#     # except Exception as e:
#     #     actual_error = f"Unexpected error: {str(e).splitlines()[2]}"
#
#     except Exception as e:
#         print(e)
#         # actual_error = f"Unexpected error: {str(e)}"
#         #
#         # actual_error = predefined_watchlist.get_login_error()
#         # # print(f"Actual error message: {actual_error}")
#         #
#         # status = "fail" if actual_error else "pass"
#
#
# def test_watch_list_tab(browserInstance):
#     driver = browserInstance
#     watchlist_tabs = LoginData(driver)
#     time.sleep(2)
#     watchlist_tabs.watchlist_tab_1()
#
#
# def test_watchlist_predefined(browserInstance):
#     driver = browserInstance
#     wait = WebDriverWait(driver, 20)
#     predefined_watchlist = predefinedWatchList(driver)
#     expected = "pass"
#
#     try:
#         time.sleep(2)
#         predefined_watchlist.predefined_watchlist_tab(test_results, expected)
#         time.sleep(2)
#         # watchlist_tabs_2.nifty_tab()
#         # time.sleep(2)
#
#         actual_error = ""  # No error if everything works
#
#     # except InvalidSelectorException as e:
#     #     actual_error = f"❌ Syntax error in XPath: {str(e)}"
#
#     except (NoSuchElementException, TimeoutException) as e:
#         actual_error = f"Element not found: {str(e)}"
#
#     # except Exception as e:
#     #     actual_error = f"Unexpected error: {str(e).splitlines()[2]}"
#
#     except Exception as e:
#         actual_error = f"Unexpected error: {str(e)}"
#
#     actual_error = predefined_watchlist.get_login_error()
#     # print(f"Actual error message: {actual_error}")
#
#     status = "fail" if actual_error else "pass"
#
#     # test_results.append({
#     #     "watchlist_bottom_tab": "",
#     #     "expected": expected,
#     #     "actual": "scrip clicked successfully" if not actual_error else f"error: {actual_error}",
#     #     "status": status
#     # })
#
#     # driver.save_screenshot(f"reports/watchlist_click_{watchlist_bottom_tab}_{status}.png")
#     assert status == expected, f"❌ Test Failed: expected {expected}, got {status}"
#     wait.until(EC.presence_of_all_elements_located(
#         (By.XPATH, "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]")))
#
#     scrip_items = driver.find_elements(By.XPATH,
#                                        "//div[contains(@class, 'mklist') and contains(@class, 'secondary-border')]")
#
#     if not scrip_items:
#         print("❌ No scrip found in watchlist.")
#         return
#
#     scrip = scrip_items[0]  # Only first scrip
#
#     try:
#         print("=== Working on First Scrip ===")
#         driver.execute_script("arguments[0].scrollIntoView(true);", scrip)
#         ActionChains(driver).move_to_element(scrip).perform()
#         time.sleep(1)
#
#         # === Click Buy ===
#         buy_button = scrip.find_element(By.XPATH, ".//button[normalize-space()='B']")
#         buy_button.click()
#         print("🟢 Clicked Buy")
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Cancel']"))).click()
#         print("❎ Cancelled Buy")
#         time.sleep(1)
#
#         # === Click Sell ===
#         ActionChains(driver).move_to_element(scrip).perform()
#         sell_button = scrip.find_element(By.XPATH, ".//button[normalize-space()='S']")
#         sell_button.click()
#         print("🔴 Clicked Sell")
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Cancel']"))).click()
#         print("❎ Cancelled Sell")
#         time.sleep(1)
#
#         # === Click Chart ===
#         ActionChains(driver).move_to_element(scrip).perform()
#         chart_buttons = scrip.find_elements(By.XPATH, ".//button")
#         if len(chart_buttons) >= 3:
#             chart_buttons[2].click()
#             print("📊 Clicked Chart")
#             time.sleep(2)
#
#         # === Click 3-dot menu (More Options) ===
#         ActionChains(driver).move_to_element(scrip).perform()
#         menu_button = scrip.find_element(By.XPATH, ".//button[contains(@id, '_opt_btn')]")
#         menu_button.click()
#         print("☰ Opened More Options")
#         time.sleep(1)
#
#         # === Click Info and close popup ===
#         info_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//span[normalize-space()='Info']/ancestor::button")))
#         info_button.click()
#         print("ℹ️ Clicked Info")
#         time.sleep(2)
#
#         close_info = wait.until(EC.element_to_be_clickable((
#             By.XPATH, "//button[@type='button' and contains(@class, 'cancel_btn') and text()='Close']")))
#         close_info.click()
#         print("❎ Closed Info")
#
#         time.sleep(5)
#         ActionChains(driver).move_to_element(scrip).perform()
#         menu_button = scrip.find_element(By.XPATH, ".//button[contains(@id, '_opt_btn')]")
#         menu_button.click()
#         print("☰ Opened More Options")
#         time.sleep(1)
#
#         company_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//span[normalize-space()='Company Details']/ancestor::button")))
#         company_button.click()
#         print("ℹ️ Clicked Info")
#         time.sleep(2)
#
#         close_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//span[contains(@class, 'br-modal-close') and text()='×']")))
#         close_button.click()
#         print("ℹ️ Clicked Info")
#         time.sleep(2)
#
#
#
#     except Exception as e:
#         print("❌ Error while processing first scrip:", e)


# def test_order_window(browserInstance):
#     driver = browserInstance
#     expected = "pass"
#     wait = WebDriverWait(driver, 20)
#     order_window = orderWindowPage(driver)
#     order_window.orderWindow(test_results, expected)
# order_window.orderWindow_Sell(test_results, expected)


# def test_dashboard(browserInstance):
#     driver = browserInstance
#     expected = "pass"
#     wait = WebDriverWait(driver, 20)
#     dashboard = dashBoardPage(driver)
#     dashboard.dashboard_header(test_results, expected)


# def test_order_book(browserInstance):
#     driver = browserInstance
#     expected = "pass"
#     wait = WebDriverWait(driver, 20)
#     order_book = OrderBook(driver)
#     order_book.order_button(test_results, expected)
#     order_book.order_list(test_results, expected)

def test_funds(browserInstance):
    driver = browserInstance
    expected = "pass"
    wait = WebDriverWait(driver, 20)
    funds_page = FundsPage(driver)
    funds_page.funds_button(test_results, expected)


def test_explore(browserInstance):
    driver = browserInstance
    expected = "pass"
    wait = WebDriverWait(driver, 20)
    explore_page = ExplorePage(driver)
    explore_page.explore_button(test_results, expected)


if __name__ == "__main__":
    pytest.main(["-v", "test_e2eTestFramework.py"])
