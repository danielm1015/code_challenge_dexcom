from environment import *
import json
from selenium import webdriver

browser = config_data['browser']['driver']

if browser == 'chrome':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r"C:\Users\Daniel.Martinez\Downloads\chromedriver.exe",
                                options=options)