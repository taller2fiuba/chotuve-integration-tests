from behave import *

from verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

REACCIONES = {
    "me gusta": 'me-gusta',
    "no me gusta": 'no-me-gusta'
}

REACCIONES_VIDEO = {
    "me gusta": 'me-gustas',
    "no me gusta": 'no-me-gustas'
}

@when('reacciono "{reaccion}" al video')
def step_impl(context, reaccion):
    context.execute_steps('Given inicie sesión correctamente')
    context.response = ChotuveAppServerApiClient().get_videos(context)
    verificar_codigo_de_respuesta(context, 200)
    context.video_id = context.response.json()[0]['id']
    reaccion_json = REACCIONES[reaccion]
    response = ChotuveAppServerApiClient().reaccionar(context.video_id, 
        reaccion_json, context)
    assert 200 <= response.status_code <= 201, f'Código de estado incorrecto: {response.status_code}'
    
@then('veo que el video tiene {cantidad:d} "{reaccion}"')
def step_impl(context, cantidad, reaccion):
    context.response = ChotuveAppServerApiClient().get_video_por_id(context.video_id, context)
    verificar_codigo_de_respuesta(context, 200)

    assert context.response.json()[REACCIONES_VIDEO[reaccion]] == cantidad, context.response.json()

@then('veo que yo reaccioné "{reaccion}"')
def step_impl(context, reaccion):
    context.execute_steps('Given inicie sesión correctamente')
    context.response = ChotuveAppServerApiClient().get_video_por_id(context.video_id, context)
    verificar_codigo_de_respuesta(context, 200)

    assert context.response.json()['mi-reaccion'] == REACCIONES[reaccion]

@then('veo que yo no reaccioné')
def step_impl(context):
    context.execute_steps('Given inicie sesión correctamente')
    context.response = ChotuveAppServerApiClient().get_video_por_id(context.video_id, context)
    verificar_codigo_de_respuesta(context, 200)

    assert context.response.json()['mi-reaccion'] == None

@given('el usuario con email "{email}" reaccionó "{reaccion}" al video')
def step_impl(context, email, reaccion):
    context.response = ChotuveAppServerApiClient().registrarse(email, "PASSWORD")
    verificar_codigo_de_respuesta(context, 201)
    context.token = context.response.json()['auth_token']
    context.response = ChotuveAppServerApiClient().get_videos(context)
    verificar_codigo_de_respuesta(context, 200)
    context.video_id = context.response.json()[0]['id']
    reaccion_json = REACCIONES[reaccion]
    response = ChotuveAppServerApiClient().reaccionar(context.video_id, 
        reaccion_json, context)
    assert 200 <= response.status_code <= 201, f'Código de estado incorrecto: {response.status_code}'

@given('reaccioné "{reaccion}" al video')
def step_impl(context, reaccion):
    context.execute_steps(f'When reacciono "{reaccion}" al video')