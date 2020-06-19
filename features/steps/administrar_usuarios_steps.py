from behave import *

from config import CHOTUVE_APP_URL
from config_usuario import EMAIL, PASSWORD
from verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient
from src.chotuve_auth_server_api_client import ChotuveAuthServerApiClient

@given('se crearon {cantidad:d} usuarios')
def step_impl(context, cantidad):
    context.usuarios = []
    for i in range(cantidad):
        context.response = ChotuveAppServerApiClient().registrarse(str(i) + EMAIL, PASSWORD)
        verificar_codigo_de_respuesta(context, 201)
        context.usuarios.append(context.response.json()['auth_token'])
    
    if cantidad > 0:
        context.usuario_id = ChotuveAuthServerApiClient().obtener_id(context.usuarios[0])
    

@when('veo los usuarios desde el web admin')
def step_impl(context):
    context.response = ChotuveAuthServerApiClient().obtener_usuarios()

@then('veo que hay {cantidad:d} usuarios')
def step_impl(context, cantidad):
    assert len(context.response.json()) == cantidad

@when('"{accion}" al usuario desde el web admin')
def step_impl(context, accion):
    data = {}
    if accion == 'habilito':
        data['habilitado'] = True
    elif accion == 'deshabilito':
        data['habilitado'] = False
    else:
        assert False, "La acción no está implementada"
    
    context.response = ChotuveAuthServerApiClient().actualizar_usuario(context.usuario_id, data)
    verificar_codigo_de_respuesta(context, 200)

@then('veo que el usuario está "{estado}"')
def step_impl(context, estado):
    context.response = ChotuveAuthServerApiClient().obtener_usuario(context.usuario_id)
    verificar_codigo_de_respuesta(context, 200)
    data = context.response.json()
    if estado == 'habilitado':
        assert data['habilitado']
    elif estado == 'deshabilitado':
        assert not data['habilitado']
    else:
        assert False, "Estado no implementado"

@given('hay un usuario deshabilitado')
def step_impl(context):
    context.execute_steps('Given se crearon 1 usuarios')
    context.execute_steps('When "deshabilito" al usuario desde el web admin')

@when('el usuario inicia sesión')
def step_impl(context):
    context.response = ChotuveAppServerApiClient().iniciar_sesion(str(0) + EMAIL, PASSWORD)

@then('ve error indicando que no está autorizado')
def step_impl(context):
    verificar_codigo_de_respuesta(context, 400)