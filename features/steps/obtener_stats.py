from behave import *
import requests

from util.asserts import assert_status_code
from util.chotuve.config import CHOTUVE_APP_URL


@given('reacciono al video')
def step_impl(context):
    context.execute_steps('When reacciono "me gusta" al video')

@when('veo las estadisticas')
def step_impl(context):
    response = requests.get(CHOTUVE_APP_URL+'/stats/historico')
    context.stats = response.json()
    assert_status_code(200, response.status_code)

@then('veo que hay {cantidad:d} reaccion')
def step_impl(context, cantidad):
    assert context.stats["total_reacciones"] == cantidad

@then('veo que hay {cantidad:d} contactos')
def step_impl(context, cantidad):
    assert context.stats["total_contactos"] == cantidad

@given('acepto la solicitud de contacto')
def step_impl(context):
    context.execute_steps('When acepto la solicitud de contacto')
