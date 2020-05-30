from behave import *

from config import CHOTUVE_APP_URL
from config_usuario import EMAIL, PASSWORD
from verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

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
    context.response = ChotuveAppServerApiClient().iniciar_sesion(EMAIL, 'no_es_mi_pass')

@when('inicio sesion con mi mail y contraseña correctos')
def step_impl(context):
    response = ChotuveAppServerApiClient().iniciar_sesion(EMAIL, PASSWORD)
    context.response = response
    context.token = response.json().get('auth_token', None)

@then('ingreso exitosamente a mi cuenta')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 200)
    assert context.response.json()['auth_token'] != ''

@then('veo error de inicio de sesión porque el mail o la contraseña es incorrecto')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 400)
    assert context.response.json()['mensaje'] == 'Email o constraseña invalidos'
