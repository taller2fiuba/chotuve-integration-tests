from behave import *

from config import CHOTUVE_APP_URL
from verificar_respuestas import *
from src.chotuve_app_server_api_client import ChotuveAppServerApiClient

@when('veo los datos de mi perfil')
def step_impl(context):
	context.response = ChotuveAppServerApiClient().get_con_token("/usuario/perfil", context)
	verificar_codigo_de_respuesta(context, 200)

@Then('veo mi nombre "{nombre}" y apellido "{apellido}"')
def step_impl(context, nombre, apellido):
	assert context.response.json()["nombre"] == nombre
	assert context.response.json()["apellido"] == apellido

@Then('veo mi mail "{mail}"')
def step_impl(context, mail):
	assert context.response.json()["email"] == mail

@Given('completé los campos de mi perfil con nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}"')
def step_impl(context, nombre, apellido, telefono, direccion):
	datos = {
		"nombre": nombre,
		"apellido": apellido,
		"telefono": telefono,
		"direccion": direccion
	}
	context.response = ChotuveAppServerApiClient().put_con_token("/usuario/perfil", datos, context)
	verificar_codigo_de_respuesta(context, 200)

@Then('veo mi nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}" y email "{mail}"')
def step_impl(context, nombre, apellido, telefono, direccion, mail):
	assert context.response.json()["nombre"] == nombre
	assert context.response.json()["apellido"] == apellido
	assert context.response.json()["telefono"] == telefono
	assert context.response.json()["direccion"] == direccion
	assert context.response.json()["email"] == mail

@Given('completé los campos de mi perfil con nombre "{nombre}", apellido "{apellido}"')
def step_impl(context, nombre, apellido):
	datos = {
		"nombre": nombre,
		"apellido": apellido,
		"telefono": None,
		"direccion": None
	}
	context.response = ChotuveAppServerApiClient().put_con_token("/usuario/perfil", datos, context)
	verificar_codigo_de_respuesta(context, 200)

@Then('veo mi nombre "{nombre}", apellido "{apellido}" y email "{mail}"')
def step_impl(context, nombre, apellido, mail):
	assert context.response.json()["nombre"] == nombre
	assert context.response.json()["apellido"] == apellido
	assert context.response.json()["email"] == mail

@Given('el usuario con email "{mail}" modifico su perfil con nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}"')
def step_impl(context, mail, nombre, apellido, telefono, direccion):
	context.response = ChotuveAppServerApiClient().registrarse(mail, "PASSWORD")
	verificar_codigo_de_respuesta(context, 201)
	response = ChotuveAppServerApiClient().iniciar_sesion(mail, "PASSWORD")
	verificar_codigo_de_respuesta(context, 201)
	context.response = response
	context.token = response.json().get('auth_token', None)
	response = ChotuveAppServerApiClient().get_con_token("/usuario/perfil", context)
	verificar_codigo_de_respuesta(context, 200)
	context.id_otro_usuario = response.json().get('id', None)
	datos = {
		"nombre": nombre,
		"apellido": apellido,
		"telefono": telefono,
		"direccion": direccion
	}
	context.response = ChotuveAppServerApiClient().put_con_token("/usuario/perfil", datos, context)
	verificar_codigo_de_respuesta(context, 200)

	@When('veo los datos del perfil del usuario con email otrousuario@otro.com')
	def step_impl(context):
		otro_usuario_id = str(context.id_otro_usuario)
		context.response = ChotuveAppServerApiClient().get_con_token("/usuario/perfil/"+otro_usuario_id, context)
		verificar_codigo_de_respuesta(context, 200)

@Then('veo su nombre "{nombre}", apellido "{apellido}", teléfono "{telefono}", dirección "{direccion}" y email "{mail}"')
def step_impl(context, nombre, apellido, telefono, direccion, mail):
	assert context.response.json()["nombre"] == nombre
	assert context.response.json()["apellido"] == apellido
	assert context.response.json()["telefono"] == telefono
	assert context.response.json()["direccion"] == direccion
	assert context.response.json()["email"] == mail
