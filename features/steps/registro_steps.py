from behave import *

from config import CHOTUVE_APP_URL
from config_usuario import EMAIL, PASSWORD
from comun_steps import verificar_codigo_de_respuesta
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

@given('mi mail ya se encuentra registrado')
def step_impl(context):
    context.execute_steps(u"""
        When me registro con mail y contraseña
    """)

@when('me registro con mail y contraseña')
def step_impl(context):
    context.response = ChotuveAppServerApiClient().registrarse(EMAIL, PASSWORD)

@then('me registro exitosamente')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 201)

@then('veo error de registro porque el mail ya está en uso')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 400)
    assert context.response.json()['errores']['email'] == 'El mail ya se encuentra registrado'
