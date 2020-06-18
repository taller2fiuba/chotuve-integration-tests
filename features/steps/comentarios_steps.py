from behave import *

from config_usuario import EMAIL
from verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

@when('comento "{comentario}" en un video')
def step_impl(context, comentario):
    context.execute_steps('Given inicie sesión correctamente')
    context.response = ChotuveAppServerApiClient().get_videos(context)
    verificar_codigo_de_respuesta(context, 200)
    context.video_id = context.response.json()[0]['id']
    context.response = ChotuveAppServerApiClient().comentar(context.video_id, 
        comentario, context)
    verificar_codigo_de_respuesta(context, 201)
    
@then('veo que hay un comentario mio que dice "{comentario}"')
def step_impl(context, comentario):
    context.response = ChotuveAppServerApiClient().obtener_comentarios(context.video_id, context)
    verificar_codigo_de_respuesta(context, 200)

    assert len(context.response.json()) == 1
    assert context.response.json()[0]["autor"]["email"] == EMAIL
    assert context.response.json()[0]["comentario"] == comentario

@given('el usuario "{email_usuario}" comentó "{comentario}"')
def step_impl(context, email_usuario, comentario):
    context.response = ChotuveAppServerApiClient().registrarse(email_usuario, "PASSWORD")
    verificar_codigo_de_respuesta(context, 201)
    context.token = context.response.json()['auth_token']
    context.response = ChotuveAppServerApiClient().get_videos(context)
    verificar_codigo_de_respuesta(context, 200)
    context.video_id = context.response.json()[0]['id']
    
    context.response = ChotuveAppServerApiClient().comentar(context.video_id, 
                                                            comentario, context)
    verificar_codigo_de_respuesta(context, 201)

@then('veo que hay {cantidad:d} comentarios')
def step_impl(context, cantidad):
    context.response = ChotuveAppServerApiClient().obtener_comentarios(context.video_id, context)
    verificar_codigo_de_respuesta(context, 200)
    assert len(context.response.json()) == cantidad

@then('veo que hay un comentario que dice "{comentario}" del usuario "{email_usuario}"')
def step_impl(context, comentario, email_usuario):
    context.response = ChotuveAppServerApiClient().obtener_comentarios(context.video_id, context)
    verificar_codigo_de_respuesta(context, 200)


    assert any(c["autor"]["email"] == email_usuario and \
               c["comentario"] == comentario \
               for c in context.response.json())