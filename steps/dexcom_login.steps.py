import time
from behave import *
from pages.Dexcom_Clarity import DexcomClarity
from pages.Home_User_Login import HomeUserLogin
from pages.Web import Browser


@given('we are on "{}"')
def get_web_page(context, url):
    Browser().load(context, url)
    time.sleep(3)


@when('user "{}" logs in')
def user_login(context, username):
    DexcomClarity().home_user_btn(context).click()
    print("clicked home_user")
    time.sleep(3)
    HomeUserLogin().login(context,username)
    print("logged in")


@then('user is authorized')
def step_impl(context):
    Browser().close(context)
