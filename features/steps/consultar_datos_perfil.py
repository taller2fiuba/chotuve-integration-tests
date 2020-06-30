from behave import *

from util.chotuve import ChotuveAppClient

@when('veo los datos de mi perfil')
def step_impl(context):
    context.data = context.yo.obtener_mi_perfil()

@Then('veo mi nombre "{nombre}" y apellido "{apellido}"')
def step_impl(context, nombre, apellido):
    assert context.data["nombre"] == nombre
    assert context.data["apellido"] == apellido

@Then('veo mi mail "{mail}"')
def step_impl(context, mail):
    assert context.data["email"] == mail

@Given('completé los campos de mi perfil con nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}", foto "{foto}"')
def step_impl(context, nombre, apellido, telefono, direccion, foto):
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "foto": foto
    }
    
    context.yo.actualizar_perfil(datos)

@Then('veo mi nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}", email "{mail}" y foto "{foto}"')
def step_impl(context, nombre, apellido, telefono, direccion, mail, foto):
    assert context.data["nombre"] == nombre
    assert context.data["apellido"] == apellido
    assert context.data["telefono"] == telefono
    assert context.data["direccion"] == direccion
    assert context.data["email"] == mail
    assert context.data["foto"] == foto

@Given('completé los campos de mi perfil con nombre "{nombre}", apellido "{apellido}"')
def step_impl(context, nombre, apellido):
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": None,
        "direccion": None,
        "foto": None
    }
    context.yo.actualizar_perfil(datos)

@Then('veo mi nombre "{nombre}", apellido "{apellido}" y email "{mail}"')
def step_impl(context, nombre, apellido, mail):
    assert context.data["nombre"] == nombre
    assert context.data["apellido"] == apellido
    assert context.data["email"] == mail

@Given('el usuario con email "{mail}" modifico su perfil con nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}", foto "{foto}"')
def step_impl(context, mail, nombre, apellido, telefono, direccion, foto):
    context.usuario = ChotuveAppClient.registrar_usuario(mail, "PASSWORD")
    
    data = context.usuario.obtener_mi_perfil()
    context.id_otro_usuario = data.get('id', None)
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "foto": foto
    }
    context.usuario.actualizar_perfil(datos)

@When('veo los datos del perfil del usuario con email otrousuario@otro.com')
def step_impl(context):
    context.data = context.yo.obtener_perfil(context.id_otro_usuario)

@Then('veo su nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}", email "{mail}" y foto "{foto}"')
def step_impl(context, nombre, apellido, telefono, direccion, mail, foto):
    assert context.data["nombre"] == nombre
    assert context.data["apellido"] == apellido
    assert context.data["telefono"] == telefono
    assert context.data["direccion"] == direccion
    assert context.data["email"] == mail
    assert context.data["foto"] == foto
