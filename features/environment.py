from behave import *

from steps.util.limpiar_base import limpiar_base_de_datos

def before_scenario(context, scenario):
    response = limpiar_base_de_datos()
    assert response.status_code == 200, 'Error al limpiar la base de datos'
