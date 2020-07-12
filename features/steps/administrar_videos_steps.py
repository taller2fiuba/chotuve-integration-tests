from behave import *

from util.chotuve_media_server_api_client import ChotuveMediaServerApiClient
from util.asserts import assert_status_code

@given(u'se crearon {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    context.execute_steps(f"Given inicie sesión correctamente")
    subir_videos(context, cantidad_videos)

@when('veo los videos')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    context.data = context.response.json()["videos"]
    assert_status_code(200, context.response.status_code)

@then(u'veo que hay {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    videos = context.data
    assert len(videos) == cantidad_videos, f'Tamaño incorrecto: {len(videos)}, esperado: {cantidad_videos}'

@when('deshabilito el video')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    assert_status_code(200, context.response.status_code)
    video_id = context.response.json()["videos"][0]["_id"]
    context.response = ChotuveMediaServerApiClient().deshabilitar_video(video_id)
    assert_status_code(200, context.response.status_code)

@then('veo que le video esta deshabilitado')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    assert_status_code(200, context.response.status_code)
    assert context.response.json()["videos"][0]["habilitado"] == False

@when('habilito el video')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    assert_status_code(200, context.response.status_code)
    video_id = context.response.json()["videos"][0]["_id"]
    context.response = ChotuveMediaServerApiClient().habilitar_video(video_id)
    assert_status_code(200, context.response.status_code)

@then('veo que el video esta habilitado')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    assert_status_code(200, context.response.status_code)
    assert context.response.json()["videos"][0]["habilitado"] == True   

@when('obtengo el muro de videos')
def step_impl(context):
    context.execute_steps(f"Given inicie sesión correctamente")
    context.data = context.yo.obtener_videos()
    videos = context.data
    assert len(videos) == 4, f'Tamaño incorrecto: {len(videos)}, esperado: {4}'

@given('hay un video deshabilitado')
def step_impl(context):
    context.execute_steps(f"""Given se crearon {1} videos""")
    context.execute_steps(f'When deshabilito el video')

@given('se deshabilito 1 video')
def step_impl(context):
    context.execute_steps(f'When deshabilito el video')

def subir_videos(context, cantidad_videos):
    context.execute_steps(f"""
        Given el usuario con email "prueba@test.com" subio {cantidad_videos} videos
    """)
