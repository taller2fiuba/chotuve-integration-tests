from behave import *

from util import assert_status_code
from util.chotuve import ChotuveAppClient

REACCIONES = {
    "me gusta": 'me-gusta',
    "no me gusta": 'no-me-gusta'
}

REACCIONES_VIDEO = {
    "me gusta": 'me-gustas',
    "no me gusta": 'no-me-gustas'
}

@when('reacciono "{reaccion}" al video')
def step_impl(context, reaccion):
    context.execute_steps('Given inicie sesión correctamente')
    context.data = context.yo.obtener_videos()
    context.video_id = context.data[0]['id']
    reaccion_json = REACCIONES[reaccion]
    response = context.yo.reaccionar_video(context.video_id, reaccion_json)
    
@then('veo que el video tiene {cantidad:d} "{reaccion}"')
def step_impl(context, cantidad, reaccion):
    context.execute_steps('Given inicie sesión correctamente')
    context.data = context.yo.obtener_video_id(context.video_id)

    assert context.data[REACCIONES_VIDEO[reaccion]] == cantidad, context.data

@then('veo que yo reaccioné "{reaccion}"')
def step_impl(context, reaccion):
    context.execute_steps('Given inicie sesión correctamente')
    context.data = context.yo.obtener_video_id(context.video_id)

    assert context.data['mi-reaccion'] == REACCIONES[reaccion]

@then('veo que yo no reaccioné')
def step_impl(context):
    context.execute_steps('Given inicie sesión correctamente')
    context.data = context.yo.obtener_video_id(context.video_id)

    assert context.data['mi-reaccion'] == None

@given('el usuario con email "{email}" reaccionó "{reaccion}" al video')
def step_impl(context, email, reaccion):
    context.usuario = ChotuveAppClient.registrar_usuario(email, "PASSWORD")
    videos = context.usuario.obtener_videos()
    context.video_id = videos[0]['id']
    reaccion_json = REACCIONES[reaccion]
    context.usuario.reaccionar_video(context.video_id, reaccion_json)

@given('reaccioné "{reaccion}" al video')
def step_impl(context, reaccion):
    context.execute_steps(f'When reacciono "{reaccion}" al video')