from behave import *

from steps.verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

def before_scenario(context, scenario):
    context.response = ChotuveAppServerApiClient().limpiar_base_de_datos()
    verificar_codigo_de_respuesta(context, 200)
