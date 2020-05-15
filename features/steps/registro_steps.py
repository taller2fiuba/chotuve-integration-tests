from behave import *
import requests

from config import CHOTUVE_APP_URL
from comun_steps import verificar_codigo_de_respuesta

@given('mi mail ya se encuentra registrado')
def step_impl(context):
    context.execute_steps(u"""
        When me registro con mail y contraseña
    """)

@when('me registro con mail y contraseña')
def step_impl(context):
    context.response = requests.post(f'{CHOTUVE_APP_URL}/usuario', json={'email': 'test@test.com', 'password': 'test123'})

@then('me registro exitosamente')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 201)

@then('veo error de registro porque el mail ya está en uso')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 400)
    assert context.response.json()['errores']['email'] == 'El mail ya se encuentra registrado'
