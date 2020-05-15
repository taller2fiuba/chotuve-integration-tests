from behave import *
import requests

from config import CHOTUVE_APP_URL
from config_usuario import EMAIL, PASSWORD
from comun_steps import verificar_codigo_de_respuesta

@given('inicie sesión correctamente')
def step_impl(context):
    context.execute_steps(u"""
        When me registro con mail y contraseña
        When inicio sesion con mi mail y contraseña correctos
    """)

@given('no inicie sesión')
def step_impl(context):
    pass

@when('pido mi mail')
def step_impl(context, titulo):
    # TODO poner header de token
    context.response = requests.get(f'{CHOTUVE_APP_URL}/usuario/perfil')

@then('recibo mi mail correctamente')
def step_impl(context):
    verificar_codigo_de_respuesta(context.response.status_code, 200)
    assert context.response.json()['email'] == EMAIL

@then('veo error porque primero debo iniciar sesión')
def step_impl(context):
    verificar_codigo_de_respuesta(context.response.status_code, 401)

@then('veo error porque debo volver a iniciar sesión')
def step_impl(context):
    verificar_codigo_de_respuesta(context.response.status_code, 403)
