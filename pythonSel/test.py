from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def add_scrip(driver, wait, search_scrip):
    # Locate the exact scrip by visible name
    scrip_xpath = f"//div[contains(@id,'_search_scrip_name') and normalize-space(text())='{search_scrip}']"

    try:
        scrip_element = wait.until(EC.presence_of_element_located((By.XPATH, scrip_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", scrip_element)
        ActionChains(driver).move_to_element(scrip_element).perform()

        # Locate the corresponding add (+) button
        add_button_xpath = f"{scrip_xpath}/ancestor::li//button[normalize-space(text())='+']"
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_button_xpath)))
        driver.execute_script("arguments[0].click();", add_button)

        print(f"✅ Added scrip: {search_scrip}")
    except Exception as e:
        print(f"❌ Failed to add scrip '{search_scrip}': {e}")
