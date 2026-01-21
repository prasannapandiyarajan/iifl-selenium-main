import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from utils.browserutils import BrowserUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import TimeoutException


class LoginData(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.forgot_password_link = (By.XPATH, '//*[@id="loginform"]/div[2]/div[2]/div[2]/a')
        self.username_input = (By.ID, "user")
        self.password_input = (By.ID, "pass")
        self.pan_number_input = (By.ID, "pan")
        self.sign_button = (By.ID, "user_btn")
        self.otp_button = (By.ID, "user_btn")
        self.search_scrip_input = (By.ID, 'watch_search_inp')
        self.hover = (By.XPATH, "//li[contains(@class, 'searchParent')]//div[contains(@class, 'hover:bg-[#f7f7f7]')]")
        self.add_scrip = (By.XPATH,
                          "//li[@id='0_search_scrip' and .//div[@id='0_search_scrip_name'][contains(text(), 'HCL-INSYS-BE')]]//button[@id='0_search_scrip_add']")
        self.close_icon = (By.XPATH, "//div[@id='mw_search_close_container']")
        # self.risk_disclosure_button = (By.CSS_SELECTOR, "#headlessui-dialog-panel-v-10 > div.mt-\[40px\].flex.justify-center.pb-\[41px\] > button")
        self.error_msg = (By.XPATH, "//p[text()='Invalid userId or password.']")
        self.buy_button = (
            By.XPATH, "//div[contains(@class, 'hover-action-btns')]//button[normalize-space(text())='B']")
        self.sell_button = (
            By.XPATH, "(//div[contains(@class, 'mklist')]//div[contains(@class, 'hover-action-btns')]//button)[6]")
        self.cancel_button = (By.XPATH, "//button[@type='button' and contains(@class, 'grey_btn') and text()='Cancel']")
        self.menu_item = (By.XPATH, "//button[.//span[text()='Info']]")
        self.info_menu_cancel_button = (By.XPATH, "//button[@class='cancel_btn' and text()='Close']")
        self.menu_item_fundamentals = (By.XPATH, "//button[.//span[text()='Fundamentals']]")
        self.close_menu_fundamentals = (By.XPATH, "//span[contains(@class, 'br-modal-close') and text()='×']")
        self.technicals = (By.XPATH, "//button[.//span[text()='Technicals']]")
        self.close_menu_technicals = (By.XPATH, "//span[@class='text-xs-center br-modal-close']")
        self.scrip_nse = (By.XPATH, "//li[@id='0_search_scrip']//button[@id='0_search_scrip_ex' and text()='NSE']")
        self.watch_item = (By.XPATH,
                           "(//div[contains(@class, 'cursor-pointer')]//span[text()='INFOBEAN-EQ']/ancestor::div[contains(@class,'cursor-pointer')])[1]")
        self.close_id = (By.ID, "mw_search_close_container")
        self.add_bottom_tab_2 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(2) span:nth-child(1)")
        self.add_bottom_tab_3 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(3) span:nth-child(1)")
        self.add_bottom_tab_4 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(4) span:nth-child(1)")
        self.add_bottom_tab_5 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(5) span:nth-child(1)")
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

        # self.cursor_button_2 = (By.XPATH, "(//div[@class='flex items-center justify-between']//button)[2] ")
        self.close_button = (By.CSS_SELECTOR,
                             "button[class='size-8 bg-[#0d45930f] text-center primaryColor mr-2 cursor-pointer flex justify-center items-center rounded']")
        self.watchlist_input_field = (By.ID, "renameInp_0")
        self.watchlist_input_field_2 = (By.ID, "renameInp_1")
        self.watchlist_input_field_3 = (By.ID, "renameInp_2")
        self.watchlist_input_field_4 = (By.ID, "renameInp_3")
        self.watchlist_input_field_5 = (By.ID, "renameInp_4")
        self.add_scrips = (By.CSS_SELECTOR,
                           "button[class='size-8 bg-[#44b748] border-[#44b748] flex justify-center items-center rounded text-center text-white cursor-pointer']")
        # self.nse_button = (By.ID, "//button[text()='NSE']")
        # self.second_scrip = (By.XPATH, "//div[text()='watchlist2']")
        # self.third_scrip = (By.XPATH, "//div[text()='watchlist2']")
        # self.fourth_scrip = (By.XPATH, "//div[text()='watchlist']")
        # self.fivth_scrip = (By.XPATH, "//div[text()='watchlist2']")

        self.add_bottom_tab_2 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(2) span:nth-child(1)")
        self.add_bottom_tab_3 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(3) span:nth-child(1)")
        self.add_bottom_tab_4 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(4) span:nth-child(1)")
        self.add_bottom_tab_5 = (By.CSS_SELECTOR, "div[id='watch_dash_group'] a:nth-child(5) span:nth-child(1)")

        self.collapse_button = (
            By.CSS_SELECTOR, "#watch_group > div > div.border-b.border-secondary.flex.gap-2 > button")

        self.collapse_button_expand = (By.XPATH, '//*[@id="app_group"]/div[2]/div[1]/div/section[1]/div/div/button')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).clear()
        # self.driver.find_element(*self.username_input).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        # self.driver.find_element(*self.risk_disclosure_button).click()

    def search_data(self, search_scr):
        self.driver.find_element(*self.search_scrip_input).clear()
        # self.driver.find_element(*self.username_input).send_keys(username)
        WebDriverWait(self.driver, 12).until(
            EC.presence_of_element_located(self.search_scrip_input)
        ).send_keys(search_scr)
        time.sleep(1)

        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.add_scrip)
        # ).click()
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.close_icon)
        # ).click()
        # hover_div = self.driver.find_element(By.XPATH,
        #                                 "//li[contains(@class, 'searchParent')]//div[contains(@class, 'hover:bg-[#f7f7f7]')]")
        # add_button = self.driver.find_element(By.XPATH, "//button[@id='0_search_scrip_add']")
        #
        # ActionChains(self.driver).move_to_element(hover_div).pause(1).click(add_button).perform()

        # time.sleep(10)

        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.watch_item)
        # ).click()
        # time.sleep(1)

        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.close_id)
        # ).click()
        #
        # time.sleep(3)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.scrip_nse)
        # ).click()
        # time.sleep(1)
        #

        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.buy_button)
        # ).click()
        # time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.cancel_button)
        # ).click()
        # time.sleep(1)

        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.sell_button)
        # ).click()
        # time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.menu_item)
        # ).click()
        # time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.C)
        # ).click()
        # time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.sell_button)
        # ).click()
        # time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.menu_item_fundamentals)
        # ).click()
        # time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.close_menu_fundamentals)
        # ).click()
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.sell_button)
        # ).click()
        # time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.technicals)
        # ).click()
        #
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.close_menu_technicals)
        # ).click()

    # def forgot_password(self, username, pannumber):
    #     try:
    #         wait = WebDriverWait(self.driver, 20)  # 10 seconds wait time
    #
    #         # Click on Forgot Password Link
    #         forgot_password_link_element = wait.until(EC.element_to_be_clickable(self.forgot_password_link))
    #         forgot_password_link_element.click()
    #
    #         # Wait for Username Input and Enter Username
    #         username_input_element = wait.until(EC.presence_of_element_located(self.username_input))
    #         username_input_element.clear()
    #         username_input_element.send_keys(username)
    #
    #         # Wait for PAN Number Input and Enter PAN Number
    #         pan_input_element = wait.until(EC.presence_of_element_located(self.pan_number_input))
    #         pan_input_element.clear()
    #         pan_input_element.send_keys(pannumber)
    #
    #         # Click on OTP Button
    #         otp_button_element = wait.until(EC.element_to_be_clickable(self.otp_button))
    #         otp_button_element.click()
    #
    #     except TimeoutException:
    #         print("Timeout waiting for element.")
    #         self.driver.save_screenshot('timeout_error.png')
    #         raise  # Re-raise to let the test fail properly
    #     # self.driver.find_element(*self.forgot_password_link).click()
    #     # self.driver.find_element(*self.username_input).clear()
    #     # self.driver.find_element(*self.username_input).send_keys(username)
    #     # self.driver.find_element(*self.pan_number_input).clear()
    #     # self.driver.find_element(*self.pan_number_input).send_keys(pannumber)
    #     # self.driver.find_element(*self.otp_button).click()
    def watchlist_tab_1(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_bottom_tab_2)
        ).click()
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_bottom_tab_3)
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_bottom_tab_4)
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_bottom_tab_5)
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.collapse_button)
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.collapse_button_expand)
        ).click()

        time.sleep(5)

    def nifty_tab(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.nifty_stock)
        ).click()
        time.sleep(5)

    def get_login_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None
