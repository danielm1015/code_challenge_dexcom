import json
import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webium import BasePage
from lib.browser import driver
from pages.Web import Browser

with open('./config.json') as json_data_file:
    config_data = json.load(json_data_file)

class DexcomClarity(BasePage):
    def __init__(self):
        return super(DexcomClarity, self).__init__()


    def home_user_btn(self, context):
        btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(@class, "btn") and contains(text(), "Dexcom CLARITY for Home Users")]')))
        assert btn, "Error locating home user button"
        return btn
        
