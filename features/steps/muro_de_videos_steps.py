from behave import *

from src.chotuve_app_server_api_client import ChotuveAppServerApiClient
from verificar_codigo_de_respuesta import *

@given('nadie subio videos')
def step_impl(context):
    pass

@when('estoy en la pantalla principal')
def step_impl(context):
    context.response = ChotuveAppServerApiClient().get_videos(context)

@then('no veo ningun video')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 200)
    assert len(context.response.json()) == 0 

@given('el usuario con email "{usuario_email}" subio {cantidad_videos:d} videos')
def step_impl(context, usuario_email, cantidad_videos):
    context.response = ChotuveAppServerApiClient().registrarse(usuario_email, "PASSWORD")
    verificar_codigo_de_respuesta(context, 201)
    context.response = ChotuveAppServerApiClient().iniciar_sesion(usuario_email, "PASSWORD")
    verificar_codigo_de_respuesta(context, 200)

    for i in range(cantidad_videos):
        context.execute_steps(u"""
            When subo un video con título "mi primer video", descripción "descripcion", ubicación "en mi casa", duracion 60 segundos y visibilidad "publico"
        """)

@then('veo sus dos videos')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 200)
    assert len(context.response.json()) == 3, f'Tamaño incorrecto: {len(context.response.json())}, esperado: {2}'