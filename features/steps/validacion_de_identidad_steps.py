from behave import *

from util import assert_status_code
from util.fixture_usuario import EMAIL, PASSWORD
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

@given('inicie sesión correctamente')
def step_impl(context):
    context.execute_steps(u"""
        When me registro con mail y contraseña
        When inicio sesion con mi mail y contraseña correctos
    """)

@given('no inicie sesión')
def step_impl(context):
    context.yo = ChotuveAppClient('')

@given('mi sesion es invalida o caduco')
def step_impl(context):
    context.yo = ChotuveAppClient('token_invalido')

@when('pido mi mail')
def step_impl(context):
    try:
        context.data = context.yo.obtener_mi_perfil()
    except ChotuveAppError as e:
        context.error = e

@then('recibo mi mail correctamente')
def step_impl(context):
    assert_status_code(200, context.yo.last_response.status_code)
    assert context.data['email'] == EMAIL

@then('veo error porque primero debo iniciar sesión')
def step_impl(context):
    assert_status_code(401, context.error.status_code)

@then('veo error porque debo volver a iniciar sesión')
def step_impl(context):
    assert_status_code(401, context.error.status_code)
