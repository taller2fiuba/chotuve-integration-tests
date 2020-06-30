from behave import *

from util import assert_status_code
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

@given('nadie subio videos')
def step_impl(context):
    pass

@when('estoy en la pantalla principal')
def step_impl(context):
    context.execute_steps(f"Given inicie sesión correctamente")
    context.data = context.yo.obtener_videos()

@then('no veo ningun video')
def step_impl(context):
    assert_status_code(200, context.yo.last_response.status_code)
    assert len(context.data) == 0 

@given('el usuario con email "{usuario_email}" subio {cantidad_videos:d} videos')
def step_impl(context, usuario_email, cantidad_videos):
    usuario = ChotuveAppClient.registrar_usuario(usuario_email, "PASSWORD")
    _subir_videos(usuario, cantidad_videos)

@given(u'yo subi {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    context.execute_steps(f"Given inicie sesión correctamente")
    _subir_videos(context.yo, cantidad_videos)

@then('veo {cantidad_videos:d} video del usuario "{usuario_email}"')
def step_impl(context, cantidad_videos, usuario_email):
    videos = context.data
    numero_videos = 0
    for video in videos:
        if video['autor']['email'] == usuario_email:
            numero_videos += 1
    
    assert numero_videos == cantidad_videos, f'Cantidad de videos incorrecta: {numero_videos}, esperado: {cantidad_videos}'

@then('veo {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    videos = context.data
    assert len(videos) == cantidad_videos, f'Tamaño incorrecto: {len(videos)}, esperado: {cantidad_videos}'

@then('veo {cantidad_videos:d} videos mas')
def step_impl(context, cantidad_videos):
    context.execute_steps(f"Then veo {cantidad_videos} videos")

@when('estoy en la pantalla principal y pido mas')
def step_impl(context):
    context.execute_steps("""
        When estoy en la pantalla principal
        Then veo 10 videos
    """)
    context.data = context.yo.obtener_videos(10)


def _subir_videos(usuario, cantidad_videos):
    for i in range(cantidad_videos):
        usuario.subir_video("https://www.testurl.com/video/1",
                            "mi primer video", 
                            60, 
                            descripcion="descripcion", 
                            ubicacion="en mi casa", 
                            visibilidad="publico")
