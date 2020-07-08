from behave import *

from util import assert_status_code
from util.fixture_usuario import EMAIL
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

ID_INVALIDO = 123456
email_usuario = "otro_usuario@test.com"

@given('otro usuario se registro')
def step_impl(context):
    context.otro_usuario = ChotuveAppClient.registrar_usuario(email_usuario, "PASSWORD")

@when('listo sus videos')
def step_impl(context):
    datos_otro_usuario = context.otro_usuario.obtener_mi_perfil()
    context.data = context.yo.obtener_videos_usuario(datos_otro_usuario["id"])#implementar en app_client.py

@given(u'otro usuario subio {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    context.execute_steps(f'Given otro usuario se registro')
    for veces in range(cantidad_videos):
        try:
            context.otro_usuario.subir_video('https://www.testurl.com/video/1', "test", 
                               60, 
                               descripcion="descripcion", 
                               ubicacion="ubicacion", 
                               visibilidad="publico")
        except ChotuveAppError as e:
            context.error = e

@Then(u'veo sus {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    assert cantidad_de_videos(context) == cantidad_videos

@given(u'subi {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    for veces in range(cantidad_videos):
        try:
            context.yo.subir_video('https://www.testurl.com/video/1', "test", 
                               60, 
                               descripcion="descripcion", 
                               ubicacion="ubicacion", 
                               visibilidad="publico")
        except ChotuveAppError as e:
            context.error = e

@when('listo mis videos')
def step_impl(context):
    mis_datos = context.yo.obtener_mi_perfil()
    context.data = context.yo.obtener_videos_usuario(mis_datos["id"])

@Then(u'veo mis {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    assert cantidad_de_videos(context) == cantidad_videos

@Then(u'veo solo {cantidad_videos:d} de sus videos')
def step_impl(context, cantidad_videos):
    assert cantidad_de_videos(context) == cantidad_videos

@when('listo mas videos del usuario')
def step_impl(context):
    datos_otro_usuario = context.otro_usuario.obtener_mi_perfil()
    context.data = context.yo.obtener_videos_usuario(datos_otro_usuario["id"], 10)

@Then(u'veo {cantidad_videos:d} videos mas')
def step_impl(context, cantidad_videos):
    assert cantidad_de_videos(context) == cantidad_videos

@when('listo los videos de un usuario que no existe')
def step_impl(context):
  try:
    context.yo.obtener_videos_usuario(ID_INVALIDO)
  except ChotuveAppError as e:
    context.error = e

@Then('veo error porque el usuario no existe')
def step_impl(context):
    assert_status_code(404, context.error.status_code)

def cantidad_de_videos(context):
  return len(context.data)