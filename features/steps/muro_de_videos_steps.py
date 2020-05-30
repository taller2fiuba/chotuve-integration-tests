from behave import *

from src.chotuve_app_server_api_client import ChotuveAppServerApiClient
from verificar_codigo_de_respuesta import *

@given('nadie subio videos')
def step_impl(context):
    pass

@when('estoy en la pantalla principal')
def step_impl(context):
    context.execute_steps(f"Given inicie sesión correctamente")
    context.response = ChotuveAppServerApiClient().get_videos(context)

@then('no veo ningun video')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 200)
    assert len(context.response.json()) == 0 

@given('el usuario con email "{usuario_email}" subio {cantidad_videos:d} videos')
def step_impl(context, usuario_email, cantidad_videos):
    context.response = ChotuveAppServerApiClient().registrarse(usuario_email, "PASSWORD")
    verificar_codigo_de_respuesta(context, 201)
    response = ChotuveAppServerApiClient().iniciar_sesion(usuario_email, "PASSWORD")
    verificar_codigo_de_respuesta(context, 201)
    context.response = response
    context.token = response.json().get('auth_token', None)

    for i in range(cantidad_videos):
        context.execute_steps(u"""
            When subo un video con título "mi primer video", descripción "descripcion", ubicación "en mi casa", duracion 60 segundos y visibilidad "publico"
        """)


@given(u'yo subi {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    context.execute_steps(f"Given inicie sesión correctamente")
    for i in range(cantidad_videos):
        context.execute_steps(u"""
            When subo un video con título "mi primer video", descripción "descripcion", ubicación "en mi casa", duracion 60 segundos y visibilidad "publico"
        """)

@then('veo {cantidad_videos:d} video del usuario "{usuario_email}"')
def step_impl(context, cantidad_videos, usuario_email):
    verificar_codigo_de_respuesta(context, 200)
    videos = context.response.json()
    verificar_cantidad_de_videos_usuario(videos, usuario_email, cantidad_videos)

@then('veo {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    verificar_codigo_de_respuesta(context, 200)
    videos = context.response.json()
    assert len(videos) == cantidad_videos, f'Tamaño incorrecto: {len(videos)}, esperado: {cantidad_videos}'

@then('veo {cantidad_videos:d} videos mas')
def step_impl(context, cantidad_videos):
    context.execute_steps(f"Then veo {cantidad_videos} videos")

@then(u'pido mas videos')
def step_impl(context):
    context.response = ChotuveAppServerApiClient().get_mas_videos(context)

@then(u'pido demasiados videos')
def step_impl(context):
    context.response = ChotuveAppServerApiClient().get_videos_inexistentes(context)
