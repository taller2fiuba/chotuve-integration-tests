from behave import *

from util import assert_status_code
from util.chotuve_auth_server_api_client import ChotuveAuthServerApiClient

@given('inicié sesión como administrador')
def step_impl(context):
    response = ChotuveAuthServerApiClient().obtener_admin_token()
    assert_status_code(200, response.status_code)
    context.admin_token = response.json()['auth_token']

@when('creo un nuevo app server con url "{url}" y nombre "{nombre}"')
def step_impl(context, nombre, url):
    context.response = ChotuveAuthServerApiClient().registrar_app_server(url, 
                                                                         nombre, 
                                                                         context.admin_token)
    assert_status_code(201, context.response.status_code)
    context.app_id = context.response.json()['id']
    
@given('creé un nuevo app server con url "{url}" y nombre "{nombre}"')
def step_impl(context, url, nombre):
    context.execute_steps(f'When creo un nuevo app server con url "{url}" y nombre "{nombre}"')

@then('me devuelve un token')
def step_impl(context):
    assert 'token' in context.response.json()

@when('veo los app servers habilitados')
def step_impl(context):
    context.response = ChotuveAuthServerApiClient().obtener_app_servers(context.admin_token)
    assert_status_code(200, context.response.status_code)
    context.data = context.response.json()

@then('veo que los app servers habilitados son "{urls}"')
def step_impl(context, urls):
    for url in urls.split(', '):
        encontrado = False
        
        for app_server in context.data:
            if url == app_server['url']:
                encontrado = True
        print(context.data)
        assert encontrado

@when('elimino el app server con nombre "{nombre}"')
def step_impl(context, nombre):
    context.response = ChotuveAuthServerApiClient().eliminar_app_server(context.app_id, 
                                                                        context.admin_token)
    assert_status_code(200, context.response.status_code)

@then('veo que no hay app servers habilitados')
def step_impl(context):
    assert len(context.data) == 0