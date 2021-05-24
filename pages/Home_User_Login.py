import json
import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from environment import *
from lib.browser import driver
from webium import BasePage


class HomeUserLogin(BasePage):
    def __init__(self):
        return super(HomeUserLogin, self).__init__()


    def login(self, context, username):
        username_textfield = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
        assert username_textfield, "Error locating username textfield"
        
        password_textfield = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        assert password_textfield, "Error locating home password textfield"

        login_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@value="Login"]')))
        assert login_btn, "Error locating login button"

        username_textfield.click()
        username_textfield.send_keys(username)
        password_textfield.click()
        password_textfield.send_keys(os.path.expandvars(config_data["passwords"][username]))
        login_btn.click()

