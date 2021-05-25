import time
from behave import *
from lib.Dexcom_Clarity_API import DexcomClarityAPI

@given('"{}" endpoint')
def step_impl(context, call):
    context.api = DexcomClarityAPI(call)
    context.api._rest_get(context, call)
    context.api._rest_post(context, call)


@when('post to call "{}"')
def step_impl(context, call):
    pass


@then('analysis in None')
def step_impl(context):
    pass
