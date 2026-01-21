import csv
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection"
    )


@pytest.fixture(scope="session")
def browserInstance(request):
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)

    driver.implicitly_wait(5)
    driver.get("https://markets.iiflcapital.com/")
    # ❌ DO NOT USE maximize_window in Docker/headless

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(
                os.path.dirname(__file__),
                "reports"
            )
            os.makedirs(reports_dir, exist_ok=True)

            file_name = os.path.join(
                reports_dir,
                report.nodeid.replace("::", "_") + ".png"
            )

            driver.save_screenshot(file_name)

            html = (
                '<div><img src="%s" alt="screenshot" '
                'style="width:304px;height:228px;" '
                'onclick="window.open(this.src)" '
                'align="right"/></div>' % file_name
            )
            extra.append(pytest_html.extras.html(html))

        report.extras = extra


def pytest_sessionfinish(session, exitstatus):
    from test_e2eTestFramework import test_results

    with open("login_test_results.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "username", "password", "conformpassword",
                "pannumber", "otp", "scrip_name",
                "Watchlist_tab", "watchlist_bottom_tab",
                "Testing_Area", "Page", "order_type",
                "validity", "expected", "actual", "status"
            ]
        )
        writer.writeheader()
        writer.writerows(test_results)