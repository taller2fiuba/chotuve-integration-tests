import requests

from .chotuve.config import CHOTUVE_AUTH_URL

class ChotuveAuthServerApiClient:
    def obtener_usuarios(self):
        return requests.get(f'{CHOTUVE_AUTH_URL}/usuario')
    
    def obtener_usuario(self, id):
        return requests.get(f'{CHOTUVE_AUTH_URL}/usuario/{id}')
    
    def obtener_id(self, auth_token):
        headers = {'Authorization': f'Bearer {auth_token}'}
        response = requests.get(f'{CHOTUVE_AUTH_URL}/usuario/sesion', headers=headers)
        assert response.status_code == 200, f'Error status code {response.status_code}'
        return response.json()['usuario_id']
    
    def actualizar_usuario(self, usuario_id, data):
        return requests.put(f'{CHOTUVE_AUTH_URL}/usuario/{usuario_id}', json=data)
    