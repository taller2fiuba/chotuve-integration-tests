from behave import *

def verificar_codigo_de_respuesta(context, codigo):
    assert context.response.status_code == codigo, f'Código de retorno incorrecto: {context.response.status_code}, esperado: {codigo}'
