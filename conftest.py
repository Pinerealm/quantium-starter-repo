import pytest
from selenium.webdriver.chrome.options import Options


# This hook allows customizing Selenium options used by dash_duo
@pytest.hookimpl(tryfirst=True)
def pytest_setup_options():
    options = Options()
    # Use the new headless mode
    options.add_argument("--headless=new")
    # The --no-sandbox argument is often necessary in containerized environments
    options.add_argument("--no-sandbox")
    # The --disable-dev-shm-usage argument can help prevent crashes in containers
    # options.add_argument("--disable-dev-shm-usage")
    # You might need to specify a unique user data directory if the default is locked
    # options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    # You can also specify the binary location if needed, though usually not required if Chrome is in PATH
    # options.binary_location = "/path/to/chrome"
    return options
