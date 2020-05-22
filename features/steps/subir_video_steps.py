from behave import *

from config import CHOTUVE_APP_URL
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

@when('intento subir un video con título "{titulo}"')
def step_impl(context, titulo):
    context.response = ChotuveAppServerApiClient().subir_video('https://www.testurl.com/video/1', titulo, context)

@then('obtiene una respuesta exitosa')
def step_impl(context):
    assert context.response.status_code == 201, f'Código de retorno incorrecto: {context.response.status_code}'
