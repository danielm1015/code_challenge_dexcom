from webium import BasePage
from lib.browser import driver
# from Dexcom_Login import DexcomLogin

class Browser(BasePage):
    def __init__(self):
        return super(Browser, self).__init__()


    def load(self, context, url):
        driver.get(url)


    def close(self, context):
        driver.quit()
