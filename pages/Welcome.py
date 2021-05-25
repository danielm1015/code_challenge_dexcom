import logging
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webium import BasePage

from lib.browser import driver

class WelcomePage(BasePage):
    def __init__(self):
        return super(WelcomePage, self).__init__()

    def home_center_text(self, context):
        h1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '// *[contains(@class, "main-content")]//h1')))
        logging.debug("h1", h1.text)
        assert h1.text, "Error locating h1 element"
        return h1.text

    


