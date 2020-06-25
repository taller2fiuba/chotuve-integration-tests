from behave import *

from util import assert_status_code
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

@when('subo un video con título "{titulo}", descripción "{descripcion}", ubicación "{ubicacion}", duracion {duracion:d} segundos y visibilidad "{visibilidad}"')
def step_impl(context, titulo, descripcion, ubicacion, duracion, visibilidad):
    _subir_video(context, titulo, duracion, descripcion, ubicacion, visibilidad)

@when('subo un video con título "{titulo}", sin descripción, ubicación "{ubicacion}", duracion {duracion:d} segundos y visibilidad "{visibilidad}"')
def step_impl(context, titulo, ubicacion, duracion, visibilidad):
    _subir_video(context, titulo, duracion, "", ubicacion, visibilidad)

@when('subo un video sin título, con descripción "{descripcion}", ubicación "{ubicacion}", duracion {duracion:d} segundos y visibilidad "{visibilidad}"')
def step_impl(context, descripcion, ubicacion, duracion, visibilidad):
    _subir_video(context, "", duracion, descripcion, ubicacion, visibilidad)

@then('obtiene una respuesta exitosa')
def step_impl(context):
    assert_status_code(201, context.yo.last_response.status_code)

@then('veo error porque la información no es válida')
def step_impl(context):
    assert_status_code(400, context.error.status_code)

def _subir_video(context, titulo, duracion, descripcion, ubicacion, visibilidad):
    try:
        context.yo.subir_video('https://www.testurl.com/video/1', titulo, 
                               duracion, 
                               descripcion=descripcion, 
                               ubicacion=ubicacion, 
                               visibilidad=visibilidad)
    except ChotuveAppError as e:
        context.error = e