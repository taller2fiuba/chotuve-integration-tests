from behave import *
import requests

from config import CHOTUVE_APP_URL
from config_usuario import EMAIL, PASSWORD
from comun_steps import verificar_codigo_de_respuesta

@given('estoy registrado')
def step_impl(context):
    context.execute_steps(u"""
        When me registro con mail y contraseña
    """)

@given('no estoy registrado')
def step_impl(context):
    pass

@when('inicio sesion con mi mail o contraseña incorrectos')
def step_impl(context, titulo):
    context.response = requests.post(f'{CHOTUVE_APP_URL}/usuario/sesion', json={'email': EMAIL, 'password': 'no_es_mi_pass'})

@when('inicio sesion con mi mail y contraseña correctos')
def step_impl(context, titulo):
    context.response = requests.post(f'{CHOTUVE_APP_URL}/usuario/sesion', json={'email': EMAIL, 'password': PASSWORD})

@then('ingreso exitosamente a mi cuenta')
def step_impl(context):
    verificar_codigo_de_respuesta(context.response.status_code, 200)
    assert context.response.json()['token'] != ''

@then('veo error de inicio de sesión porque el mail o la contraseña es incorrecto')
def step_impl(context):
    verificar_codigo_de_respuesta(context.response.status_code, 400)
    assert context.response.json()['mensaje'] == 'Email o constraseña invalidos'
