from behave import *

from util import assert_status_code
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

VIDEO_ID_INVALIDO = "video-id-invalido"

@when(u'pido el video')
def step_impl(context):
    context.execute_steps("""
    When estoy en la pantalla principal
    Then veo 1 videos""")
    video = context.data[0]
    context.data = context.yo.obtener_video_id(video['id'])

@then('veo el video de "{email}"')
def step_impl(context, email):
    assert_status_code(200, context.yo.last_response.status_code)
    video = context.data
    assert video['autor']['email'] == email, f"Incorrecto: {video['autor']['email']}, valor esperado: {email}"

@when(u'pido por un video especifico')
def step_impl(context):
    try:
        context.data = context.yo.obtener_video_id(VIDEO_ID_INVALIDO)
    except ChotuveAppError as e:
        context.error = e

@then(u'veo error por que el video no existe')
def step_impl(context):
    assert_status_code(404, context.error.status_code)