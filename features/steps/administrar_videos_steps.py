from behave import *

from src.chotuve_app_server_api_client import ChotuveAppServerApiClient
from src.chotuve_media_server_api_client import ChotuveMediaServerApiClient
from verificar_respuestas import * 

@given(u'se crearon {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    context.execute_steps(f"Given inicie sesión correctamente")
    subir_videos(context, cantidad_videos)

@when('veo los videos')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    verificar_codigo_de_respuesta(context, 200)

@then(u'veo que hay {cantidad_videos:d} videos')
def step_impl(context, cantidad_videos):
    videos = context.response.json()
    assert len(videos) == cantidad_videos, f'Tamaño incorrecto: {len(videos)}, esperado: {cantidad_videos}'

@when('deshabilito el video')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    verificar_codigo_de_respuesta(context, 200)
    video_id = context.response.json()[0]["_id"]
    context.response = ChotuveMediaServerApiClient().deshabilitar_video(video_id)
    verificar_codigo_de_respuesta(context, 200)

@then('veo que le video esta deshabilitado')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    verificar_codigo_de_respuesta(context, 200)
    assert context.response.json()[0]["habilitado"] == False

@when('habilito el video')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    verificar_codigo_de_respuesta(context, 200)
    video_id = context.response.json()[0]["_id"]
    context.response = ChotuveMediaServerApiClient().habilitar_video(video_id)
    verificar_codigo_de_respuesta(context, 200)

@then('veo que el video esta habilitado')
def step_impl(context):
    context.response = ChotuveMediaServerApiClient().get_videos()
    verificar_codigo_de_respuesta(context, 200)
    assert context.response.json()[0]["habilitado"] == True   

@when('obtengo el muro de videos')
def step_impl(context):
    context.execute_steps(f"Given inicie sesión correctamente")
    context.response = ChotuveAppServerApiClient().get_videos(context)
    verificar_codigo_de_respuesta(context, 200)
    videos = context.response.json()
    assert len(videos) == 4, f'Tamaño incorrecto: {len(videos)}, esperado: {4}'

@given('hay un video deshabilitado')
def step_impl(context):
    context.execute_steps(f"Given inicie sesión correctamente")
    subir_videos(context, 1)
    #context.execute_steps(f'deshabilito el video')
    context.response = ChotuveMediaServerApiClient().get_videos()
    verificar_codigo_de_respuesta(context, 200)
    video_id = context.response.json()[0]["_id"]
    context.response = ChotuveMediaServerApiClient().deshabilitar_video(video_id)
    verificar_codigo_de_respuesta(context, 200)

@given('se deshabilito 1 video')
def step_impl(context):
    #context.execute_steps(f'deshabilito el video')
    context.response = ChotuveMediaServerApiClient().get_videos()
    verificar_codigo_de_respuesta(context, 200)
    video_id = context.response.json()[0]["_id"]
    context.response = ChotuveMediaServerApiClient().deshabilitar_video(video_id)
    verificar_codigo_de_respuesta(context, 200)

def subir_videos(context, cantidad_videos):
    context.execute_steps(f"""
        Given el usuario con email "prueba@test.com" subio {cantidad_videos} videos
    """)
