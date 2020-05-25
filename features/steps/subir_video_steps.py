from behave import *

from config import CHOTUVE_APP_URL
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

@when('intento subir un video con título "{titulo}", descripción "{descripcion}", ubicación "{ubicacion}" y visibilidad "{visibilidad}"')
def step_impl(context, titulo, descripcion, ubicacion, visibilidad):
    context.response = ChotuveAppServerApiClient().subir_video('https://www.testurl.com/video/1', titulo, "una descripcion", ubicacion, visibilidad, context)

@when('intento subir un video con título "{titulo}", sin descripción, ubicación "{ubicacion}" y visibilidad "{visibilidad}"')
def step_impl(context, titulo, ubicacion, visibilidad):
    context.response = ChotuveAppServerApiClient().subir_video('https://www.testurl.com/video/1', titulo, "", ubicacion, visibilidad, context)

@when('intento subir un video sin título, con descripción "{descripcion}", ubicación "{ubicacion}" y visibilidad "{visibilidad}"')
def step_impl(context, descripcion, ubicacion, visibilidad):
    context.response = ChotuveAppServerApiClient().subir_video('https://www.testurl.com/video/1', "", descripcion, ubicacion, visibilidad, context)

@then('obtiene una respuesta exitosa')
def step_impl(context):
    assert context.response.status_code == 201, f'Código de retorno incorrecto: {context.response.status_code}'

@then('veo error porque la información no es válida')
def step_impl(context):
    assert context.response.status_code == 400, f'Código de retorno incorrecto: {context.response.status_code}'

