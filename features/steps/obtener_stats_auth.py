from behave import *
import requests

from util.asserts import assert_status_code
from util.chotuve.config import CHOTUVE_AUTH_URL

@when('veo las estadisticas de usuarios')
def step_impl(context):
    response = requests.get(CHOTUVE_AUTH_URL+'/stats/historico')
    context.stats = response.json()
    assert_status_code(200, response.status_code)

@then('veo que se registraron {cantidad:d} usuarios')
def step_impl(context, cantidad):
    assert context.stats["total_usuarios"] == cantidad
