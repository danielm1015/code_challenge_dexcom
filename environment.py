import json
import logging 

from lib import browser


with open('./config.json') as json_data_file:
    config_data = json.load(json_data_file)


def after_scenario(context, scenario):
    browser.driver.quit()
