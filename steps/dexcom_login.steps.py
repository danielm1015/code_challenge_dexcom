import time
from behave import *

from environment import *
from pages.Dexcom_Clarity import DexcomClarity
from pages.Home_User_Login import HomeUserLogin
from pages.Welcome import WelcomePage
from pages.Web import Browser


@given('we are on "{}"')
def get_web_page(context, url):
    Browser().load(context, url)


@when('user "{}" logs in')
def user_login(context, username):
    DexcomClarity().home_user_btn(context).click()
    logging.info("clicked home_user")
    HomeUserLogin().login(context,username)
    logging.info("logged in")
    time.sleep(3)

@then('user is authorized')
def verify_login(context):
    WelcomePage().home_center_text(context)
    logging.info("Verified login")
    Browser().close(context)


