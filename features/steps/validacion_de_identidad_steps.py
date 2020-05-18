from behave import *

from config import CHOTUVE_APP_URL
from config_usuario import EMAIL, PASSWORD
from verificar_codigo_de_respuesta import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

@given('inicie sesión correctamente')
def step_impl(context):
    context.execute_steps(u"""
        When me registro con mail y contraseña
        When inicio sesion con mi mail y contraseña correctos
    """)

@given('no inicie sesión')
def step_impl(context):
    context.token = ''

@given('mi sesion es invalida o caduco')
def step_impl(context):
    context.token = 'token_invalido'

@when('pido mi mail')
def step_impl(context):
    context.response = ChotuveAppServerApiClient().mi_perfil(context)

@then('recibo mi mail correctamente')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 200)
    assert context.response.json()['email'] == EMAIL

@then('veo error porque primero debo iniciar sesión')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 401)

@then('veo error porque debo volver a iniciar sesión')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 401)
