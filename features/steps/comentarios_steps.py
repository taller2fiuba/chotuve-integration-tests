from behave import *

from util import assert_status_code
from util.fixture_usuario import EMAIL
from util.chotuve import ChotuveAppClient

@when('comento "{comentario}" en un video')
def step_impl(context, comentario):
    context.execute_steps('Given inicie sesión correctamente')
    context.data = context.yo.obtener_videos()
    context.video_id = context.data[0]['id']
    context.yo.comentar_video(context.video_id, comentario)
    assert_status_code(201, context.yo.last_response.status_code)
    
@then('veo que hay un comentario mio que dice "{comentario}"')
def step_impl(context, comentario):
    context.data = context.yo.obtener_comentarios_video(context.video_id)

    assert len(context.data) == 1
    assert context.data[0]["autor"]["email"] == EMAIL
    assert context.data[0]["comentario"] == comentario

@given('el usuario "{email_usuario}" comentó "{comentario}"')
def step_impl(context, email_usuario, comentario):
    usuario = ChotuveAppClient.registrar_usuario(email_usuario, "PASSWORD")
    videos = usuario.obtener_videos()
    context.video_id = videos[0]['id']
    
    usuario.comentar_video(context.video_id, comentario)
    assert_status_code(201, usuario.last_response.status_code)

@then('veo que hay {cantidad:d} comentarios')
def step_impl(context, cantidad):
    context.execute_steps('Given inicie sesión correctamente')
    context.data = context.yo.obtener_comentarios_video(context.video_id)
    assert len(context.data) == cantidad

@then('veo que hay un comentario que dice "{comentario}" del usuario "{email_usuario}"')
def step_impl(context, comentario, email_usuario):
    context.data = context.yo.obtener_comentarios_video(context.video_id)

    assert any(c["autor"]["email"] == email_usuario and \
               c["comentario"] == comentario \
               for c in context.data)