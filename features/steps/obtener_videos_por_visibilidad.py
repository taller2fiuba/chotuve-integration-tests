from behave import *

from util import assert_status_code
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError

@given('"{nombre}" es mi amigo')
def step_impl(context, nombre):
	context.execute_steps("""
		Given "edson" me mandó solicitud de contacto
        When acepto la solicitud de contacto
    """)

@given('"{nombre}" subio un video privado')
def step_impl(context, nombre):
    context.usuarios[nombre].subir_video(
        "http://www.video_test.com",
        "Alto test",
        60,
        visibilidad = "privado"
        )

@when('listo los videos de "{nombre}"')
def step_impl(context, nombre):
    nombre_id = context.usuarios_data[nombre]["id"]
    context.data = context.yo.obtener_videos_usuario(nombre_id)
