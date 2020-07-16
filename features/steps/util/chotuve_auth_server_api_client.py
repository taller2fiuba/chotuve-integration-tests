import requests

from .chotuve.config import CHOTUVE_AUTH_URL

class ChotuveAuthServerApiClient:
    def obtener_admin_token(self):
        return requests.post(f'{CHOTUVE_AUTH_URL}/usuario/admin', json={
            'email': 'admin',
            'password': 'admin'
        })

    def registrar_app_server(self, url, nombre, auth_token):
        return requests.post(f'{CHOTUVE_AUTH_URL}/app-server', 
                             headers={'Authorization': f'Bearer {auth_token}'},
                             json={'url': url, 'nombre': nombre})
                            
    def obtener_app_servers(self, auth_token):
        return requests.get(f'{CHOTUVE_AUTH_URL}/app-server',
                            headers={'Authorization': f'Bearer {auth_token}'})
                        
    def eliminar_app_server(self, app_id, auth_token):
        return requests.delete(f'{CHOTUVE_AUTH_URL}/app-server/{app_id}',
                               headers={'Authorization': f'Bearer {auth_token}'})

    def obtener_usuarios(self):
        return requests.get(f'{CHOTUVE_AUTH_URL}/usuario')
    
    def obtener_usuario(self, id):
        return requests.get(f'{CHOTUVE_AUTH_URL}/usuario/{id}')
    
    def obtener_id(self, auth_token):
        headers = {'Authorization': f'Bearer {auth_token}'}
        response = requests.get(f'{CHOTUVE_AUTH_URL}/usuario/sesion', headers=headers)
        assert response.status_code == 200, f'Error status code {response.status_code}'
        return response.json()['usuario_id']
    
    def actualizar_usuario(self, usuario_id, data, auth_token):
        return requests.put(f'{CHOTUVE_AUTH_URL}/usuario/{usuario_id}', 
                            json=data,
                            headers={'Authorization': f'Bearer {auth_token}'})
    