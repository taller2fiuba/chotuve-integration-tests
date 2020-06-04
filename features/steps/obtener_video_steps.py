from behave import *

from verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

VIDEO_ID_INVALIDO = "5ed7170d398be"

@when(u'pido el video')
def step_impl(context):
    context.execute_steps("""
    When estoy en la pantalla principal
    Then veo 1 videos""")
    video = context.response.json()[0]
    context.response = ChotuveAppServerApiClient().get_video_por_id(video['id'], context)

@then('veo el video de "{email}"')
def step_impl(context, email):
    verificar_codigo_de_respuesta(context, 200)
    video = context.response.json()
    assert video['autor']['email'] == email, f"Incorrecto: {video['autor']['email']}, valor esperado: {email}"

@when(u'pido por un video especifico')
def step_impl(context):
    context.response = ChotuveAppServerApiClient().get_video_por_id(VIDEO_ID_INVALIDO, context)


@then(u'veo error por que el video no existe')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 404)