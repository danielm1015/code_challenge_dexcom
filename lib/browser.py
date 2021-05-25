from environment import *
import json
from selenium import webdriver

browser = config_data['browser']['driver']

if browser == 'chrome':
    driver = webdriver.Chrome()