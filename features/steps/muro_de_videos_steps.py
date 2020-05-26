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
    assert context.response.json()['data'].length == 0 