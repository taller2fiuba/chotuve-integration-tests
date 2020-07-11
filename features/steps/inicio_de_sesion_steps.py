from behave import *

from util import assert_status_code
from util.fixture_usuario import EMAIL, PASSWORD
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

@given('estoy registrado')
def step_impl(context):
    context.execute_steps(u"""
        When me registro con mail y contraseña
    """)

@given('no estoy registrado')
def step_impl(context):
    pass

@when('inicio sesion con mi mail o contraseña incorrectos')
def step_impl(context):
    try:
        context.yo = ChotuveAppClient(EMAIL, 'no_es_mi_pass')
    except ChotuveAppError as e:
        context.error = e

@when('inicio sesion con mi mail y contraseña correctos')
def step_impl(context):
    try:
        context.yo = ChotuveAppClient(EMAIL, PASSWORD)
    except ChotuveAppError as e:
        context.error = e

@then('ingreso exitosamente a mi cuenta')
def step_impl(context):
    assert_status_code(200, context.yo.last_response.status_code)
    assert context.yo.auth_token != ''
    assert context.yo.id != ''

@then('veo error de inicio de sesión porque el mail o la contraseña es incorrecto')
def step_impl(context):
    assert_status_code(400, context.error.status_code)
    assert context.error.response.json()['mensaje'] == 'Email o constraseña invalidos'
