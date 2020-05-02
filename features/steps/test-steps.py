from behave import *
import requests

from config import CHOTUVE_APP_URL

@when('llamo al index')
def step_impl(context):
    pass

@then('devuelve hello world')
def step_impl(context):
    assert True
