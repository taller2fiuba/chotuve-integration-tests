from behave import *

from util import assert_status_code
from util.fixture_usuario import EMAIL, PASSWORD
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

@given('mi mail ya se encuentra registrado')
def step_impl(context):
    context.execute_steps('When me registro con mail y contraseña')

@when('me registro con mail y contraseña')
def step_impl(context):
    try:
        context.yo = ChotuveAppClient.registrar_usuario(EMAIL, PASSWORD)
    except ChotuveAppError as e:
        context.error = e

@then('me registro exitosamente')
def step_impl(context):
    assert_status_code(201, context.yo.last_response.status_code)
    assert context.yo.auth_token != ''
    assert context.yo.id != ''

@then('veo error de registro porque el mail ya está en uso')
def step_impl(context):
    assert 400 == context.error.status_code, str(context.error)
    assert context.error.response.json()['errores']['email'] == 'El mail ya se encuentra registrado', str(context.error)
