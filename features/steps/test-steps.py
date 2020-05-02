from behave import *
import requests

from config import CHOTUVE_APP_URL

@given('que estoy en la aplicación')
def step_impl(context):
    pass

@when('intento subir un video con título "{titulo}"')
def step_impl(context, titulo):
    context.response = requests.post(f'{CHOTUVE_APP_URL}/video', data = {'url': 'https://www.testurl.com/video/1', 'titulo': titulo})

@then('obtiene una respuesta exitosa')
def step_impl(context):
    context.response.status_code == 201
