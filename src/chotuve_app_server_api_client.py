import requests

from steps.config import CHOTUVE_APP_URL

class ChotuveAppServerApiClient:

    def registrarse(self, email, password):
        return self.post('usuario', {'email': email, 'password': password})

    def iniciar_sesion(self, email, password):
        return self.post('usuario/sesion', {'email': email, 'password': password})

    def mi_perfil(self, context):
        return self.get_con_token('usuario/perfil', context)

    def subir_video(self, video_url, titulo):
        return self.post('video', {'url': video_url, 'titulo': titulo})

    def limpiar_base_de_datos(self):
        return requests.delete(f'{CHOTUVE_APP_URL}/base_de_datos')

    def get_con_token(self, url, context):
        headers = {'Authorization': f'Bearer {context.token}'}
        return requests.get(f'{CHOTUVE_APP_URL}/{url}', headers=headers)

    def post(self, url, json):
        return requests.post(f'{CHOTUVE_APP_URL}/{url}', json=json)
