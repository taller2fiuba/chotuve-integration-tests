from behave import *

def verificar_codigo_de_respuesta(context, codigo):
    assert context.response.status_code == codigo, f'Código de retorno incorrecto: {context.response.status_code}, esperado: {codigo}'

def verificar_cantidad_de_videos_usuario(videos, usuario_email, cantidad):
    numero_videos = 0
    for video in videos:
        if video['autor']['email'] == usuario_email:
            numero_videos += 1
    
    assert numero_videos == cantidad, f'Cantidad de videos incorrecta: {numero_videos}, esperado: {cantidad}'