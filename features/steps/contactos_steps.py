from behave import *

from util.chotuve import ChotuveAppClient
from util.fixture_usuario import PASSWORD

@given('"{nombre}" se registró correctamente')
def step_impl(context, nombre):
    if not hasattr(context, 'usuarios'):
        context.usuarios = {}
        context.usuarios_data = {}
    context.usuarios[nombre] = ChotuveAppClient.registrar_usuario(f"{nombre}@email.com", PASSWORD)
    context.usuarios_data[nombre] = context.usuarios[nombre].obtener_mi_perfil()

@given('"{nombre}" me mandó solicitud de contacto')
def step_impl(context, nombre):
    yo = context.yo.obtener_mi_perfil()
    context.usuarios[nombre].enviar_solicitud_contacto(yo['id'])
    context.data = context.yo.obtener_solicitudes_contacto()[0]['id']

@when('veo mis solicitudes de contacto')
def step_impl(context):
    context.data = context.yo.obtener_solicitudes_contacto()

@then('veo que "{nombre}" me mandó solicitud de contacto')
def step_impl(context, nombre):
    if not any(s['email'] == f"{nombre}@email.com" for s in context.data):
        fail('%r not in %r', (f"{nombre}@email.com", context.data))

@when('veo el perfil de "{nombre}"')
def step_impl(context, nombre):
    context.data = context.yo.obtener_perfil(context.usuarios_data[nombre]['id'])

@then('veo que su solicitud de contacto está pendiente de aprobación')
def step_impl(context):
    if context.data.get('estado-contacto') != 'solicitud-pendiente':
        fail('No hay una solicitud pendiente (%r)' % context.data.get('estado-contacto'))

@given('le mandé solicitud de contacto a "{nombre}"')
def step_impl(context, nombre):
    context.yo.enviar_solicitud_contacto(context.usuarios_data[nombre]['id'])

@then('veo que mi solicitud de contacto está pendiente de aprobación')
def step_impl(context):
    if context.data.get('estado-contacto') != 'solicitud-enviada':
        fail('No hay una solicitud enviada (%r)' % context.data.get('estado-contacto'))

@when('acepto la solicitud de contacto')
def step_impl(context):
    context.yo.aceptar_solicitud_contacto(context.data)

@when('rechazo la solicitud')
def step_impl(context):
    context.yo.rechazar_solicitud_contacto(context.data)

@then('veo que es mi contacto')
def step_impl(context):
    if context.data.get('estado-contacto') != 'contacto':
        fail('No es contacto (%r)' % context.data.get('estado-contacto'))


@then('veo que no es mi contacto y que no hay solicitud pendiente')
def step_impl(context):
    if context.data.get('estado-contacto') != None:
        fail('Estado de contacto incorrecto: %r', context.data.get('estado-contacto'))

@given('"{nombre}" es mi contacto')
def step_impl(context, nombre):
    context.yo.enviar_solicitud_contacto(context.usuarios_data[nombre]['id'])
    context.data = context.usuarios[nombre].obtener_solicitudes_contacto()['solicitud_id']

@when('veo mis contactos')
def step_impl(context):
    context.data = context.yo.obtener_contactos()

@then('veo que mis contactos son "{nombres}"')
def step_impl(context, nombres):
    if len(context.data) != len(nombres.split(',')):
        fail('Hay %r contactos en lugar de %r' % (len(context.data), len(nombre.split(','))))

    for nombre in nombres.split(','):
        encontrado = False
        for contacto in context.data:
            if f'{nombre}@email.com' == contacto['email']:
                encontrado = True
                break
        
        if not encontrado:
            fail('Falta el contacto %r en %r' % (nombre, context.data))