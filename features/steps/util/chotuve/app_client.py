#!/usr/bin/env python3

'''
Cliente para pruebas de aceptación del app server.
'''

import requests

from .config import CHOTUVE_APP_URL
from .error import ChotuveAppError

class ChotuveAppClient:
    @staticmethod
    def registrar_usuario(email, clave):
        '''
        Registra un nuevo usuario en Chotuve.

        Devuelve un ChotuveAppClient asociado a ese usuario.
        '''
        response = ChotuveAppClient._post('/usuario', {
            'email': email,
            'password': clave
        })

        return ChotuveAppClient(response.json()['auth_token'], 
                                _last_response=response)

    def __init__(self, usuario_o_token, clave=None, _last_response=None):
        if not clave:
            self.auth_token = usuario_o_token
            self.last_response = _last_response
            return

        response = ChotuveAppClient._post('/usuario/sesion', {
            'email': usuario_o_token,
            'password': clave
        })

        self.auth_token = response.json()['auth_token']
        self.last_response = response

    def obtener_mi_perfil(self):
        self.last_response = self._get('/usuario/perfil', {}, self.auth_token)

        return self.last_response.json()
    
    def obtener_videos(self, offset=0, cantidad=10):
        self.last_response = self._get('/video', 
                                       {"cantidad": cantidad, "offset": offset}, 
                                       self.auth_token)
        return self.last_response.json()
    
    def obtener_video_id(self, video_id):
        self.last_response = self._get(f'/video/{video_id}', {}, self.auth_token)
        
        return self.last_response.json()
    
    def obtener_comentarios_video(self, video_id, cantidad=10, offset=0):
        self.last_response = self._get(
            f'/video/{video_id}/comentario',
            {"cantidad": cantidad, "offset": offset},
            self.auth_token
        )
        
        return self.last_response.json()
    
    def comentar_video(self, video_id, comentario):
        self.last_response = self._post(f'/video/{video_id}/comentario', 
                                        {"comentario": comentario},
                                        self.auth_token)
                
    def reaccionar_video(self, video_id, reaccion):
        if not reaccion in ('me-gusta', 'no-me-gusta'):
            raise ValueError('La reacción debe ser "me-gusta" o "no-me-gusta"')
        
        self.last_response = self._post(f'/video/{video_id}/reaccion', 
                                        {"reaccion": reaccion},
                                        self.auth_token)

    def subir_video(self, url, titulo, duracion, **kwargs):
        datos_opcionales = ('descripcion', 'ubicacion', 'visibilidad')
        datos = {
            'url': url,
            'titulo': titulo,
            'duracion': duracion
        }

        for clave in datos_opcionales:
            if clave in kwargs:
                datos[clave] = kwargs.pop(clave)
        
        if len(kwargs) != 0:
            raise ValueError('Parámetros opcionales no reconocidos: ' +\
                             ','.join(kwargs.keys()))

        self.last_response = self._post(f'/video', datos, self.auth_token)
    
    def obtener_perfil(self, usuario_id):
        response = self._get(f'/usuario/{usuario_id}/perfil', {}, self.auth_token)
        
        self.last_response = response
        return response.json()
    
    def actualizar_perfil(self, datos):
        self.last_response = self._put(f'/usuario/perfil', datos, self.auth_token)

    def aceptar_solicitud_contacto(self, solicitud_id):
        self.last_response = self._put(f'/usuario/solicitud-contacto/{solicitud_id}',
                                       {'accion': 'aceptar'}, 
                                       self.auth_token)

    def rechazar_solicitud_contacto(self, solicitud_id):
        self.last_response = self._put(f'/usuario/solicitud-contacto/{solicitud_id}',
                                       {'accion': 'rechazar'}, 
                                       self.auth_token)
    
    def enviar_solicitud_contacto(self, usuario_id):
        self.last_response = self._post('/usuario/solicitud-contacto', {
            'usuario_id': usuario_id
        }, self.auth_token)
        return self.last_response.json()
    
    def obtener_solicitudes_contacto(self):
        self.last_response = self._get('/usuario/solicitud-contacto', {}, self.auth_token)
        return self.last_response.json()

    def obtener_contactos(self, usuario_id=None):
        url = f"/usuario{'/' + str(usuario_id) if usuario_id else ''}/contacto"
        self.last_response = self._get(url, {}, self.auth_token)
        return self.last_response.json()

    @staticmethod
    def _get(url_path, params, auth_token=None):
        if not params:
            params = {}
        return ChotuveAppClient._do_http_request(requests.get, url_path, params,
                                                 {}, auth_token)

    @staticmethod
    def _post(url_path, data, auth_token=None):
        return ChotuveAppClient._do_http_request(requests.post, url_path, {}, 
                                                 data, auth_token)

    @staticmethod
    def _put(url_path, data, auth_token=None):
        return ChotuveAppClient._do_http_request(requests.put, url_path, {}, 
                                                 data, auth_token)

    @staticmethod
    def _do_http_request(method, url_path, params, json_data, auth_token=None):
        headers = {}
        if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'
        
        response =  method(CHOTUVE_APP_URL + url_path, params=params,
                           json=json_data, 
                           headers=headers)
        
        if not 200 <= response.status_code < 300:
            raise ChotuveAppError(response)
    
        return response
