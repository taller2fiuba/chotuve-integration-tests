from behave import *
import requests

from config import CHOTUVE_APP_URL

@when('intento subir un video con título "{titulo}"')
def step_impl(context, titulo):
    context.response = requests.post(f'{CHOTUVE_APP_URL}/video', json={'url': 'https://www.testurl.com/video/1', 'titulo': titulo})

@then('obtiene una respuesta exitosa')
def step_impl(context):
    assert context.response.status_code == 201, f'Código de retorno incorrecto: {context.response.status_code}'