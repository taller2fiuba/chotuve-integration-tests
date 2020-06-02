from behave import *

from config import CHOTUVE_APP_URL
from verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

@when('subo un video con título "{titulo}", descripción "{descripcion}", ubicación "{ubicacion}", duracion {duracion:d} segundos y visibilidad "{visibilidad}"')
def step_impl(context, titulo, descripcion, ubicacion, duracion, visibilidad):
    context.response = ChotuveAppServerApiClient().subir_video('https://www.testurl.com/video/1', titulo, "una descripcion", ubicacion, duracion, visibilidad, context)

@when('subo un video con título "{titulo}", sin descripción, ubicación "{ubicacion}", duracion {duracion:d} segundos y visibilidad "{visibilidad}"')
def step_impl(context, titulo, ubicacion, duracion, visibilidad):
    context.response = ChotuveAppServerApiClient().subir_video('https://www.testurl.com/video/1', titulo, "", ubicacion, duracion, visibilidad, context)

@when('subo un video sin título, con descripción "{descripcion}", ubicación "{ubicacion}", duracion {duracion:d} segundos y visibilidad "{visibilidad}"')
def step_impl(context, descripcion, ubicacion, duracion, visibilidad):
    context.response = ChotuveAppServerApiClient().subir_video('https://www.testurl.com/video/1', "", descripcion, ubicacion, duracion, visibilidad, context)

@then('obtiene una respuesta exitosa')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 201)

@then('veo error porque la información no es válida')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 400)

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
