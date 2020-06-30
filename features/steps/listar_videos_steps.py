from behave import *

from util import assert_status_code
from util.fixture_usuario import EMAIL
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

ID_INVALIDO = 123456

@given('otro usuario se registro')
def step_impl(context):
    context.otro_usuario = ChotuveAppClient.registrar_usuario(email_usuario, "PASSWORD")

@when('listo sus videos')
def step_impl(context):
    datos_otro_usuario = context.otro_usuario.obtener_mi_perfil()
    context.data = context.yo.obtener_videos_usuario(datos_otro_usuario["id"])#implementar en app_client.py

#@Then('no veo ningun video')
#def step_impl(context):
#    assert len(context.data) == 0

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
def step_impl(contex, cantidad_videos):
    assert len(context.data) == cantidad_videos

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
    datos_otro_usuario = context.otro_usuario.obtener_mi_perfil()
    context.data = context.yo.obtener_videos()

@Then(u'veo mis {cantidad_videos:d} videos')
def step_impl(contex, cantidad_videos):
    assert len(context.data) == cantidad_videos

@Then(u'veo solo {cantidad_videos:d} de sus videos')
def step_impl(contex, cantidad_videos):
    assert len(context.data) == cantidad_videos

#And listo mas videos del usuario

@when('listo los videos de un usuario que no existe')
def step_impl(context):
    datos_otro_usuario = context.otro_usuario.obtener_mi_perfil()
    context.data = context.yo.obtener_videos_usuario(ID_INVALIDO)#implementar en app_client.py

@Then('veo error porque el usuario no existe')
def step_impl(contex, cantidad_videos):
    assert_status_code(401, context.error.status_code)#chequeear el status code
