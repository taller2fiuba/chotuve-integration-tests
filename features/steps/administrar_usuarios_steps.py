from behave import *

from util import assert_status_code
from util.fixture_usuario import EMAIL, PASSWORD
from util.chotuve import ChotuveAppClient
from util.chotuve.error import ChotuveAppError
from util.chotuve_auth_server_api_client import ChotuveAuthServerApiClient

@given('se crearon {cantidad:d} usuarios')
def step_impl(context, cantidad):
    context.usuarios = []
    for i in range(cantidad):
        usuario_nuevo = ChotuveAppClient.registrar_usuario(str(i) + EMAIL, 
                                                           PASSWORD)
        context.usuarios.append(usuario_nuevo)
    
    if cantidad > 0:
        context.usuario_id = ChotuveAuthServerApiClient().obtener_id(context.usuarios[0].auth_token)
    

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
    
    response = ChotuveAuthServerApiClient().obtener_admin_token()
    assert_status_code(200, response.status_code)
    token = response.json()['auth_token']
    context.response = ChotuveAuthServerApiClient().actualizar_usuario(context.usuario_id, 
                                                                       data, 
                                                                       token)
    assert_status_code(200, context.response.status_code)

@then('veo que el usuario está "{estado}"')
def step_impl(context, estado):
    context.response = ChotuveAuthServerApiClient().obtener_usuario(context.usuario_id)
    assert_status_code(200, context.response.status_code)
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
    try:
        context.usuario = ChotuveAppClient(str(0) + EMAIL, PASSWORD)
    except ChotuveAppError as e:
        context.error = e

@then('ve error indicando que no está autorizado')
def step_impl(context):
    assert_status_code(400, context.error.status_code)