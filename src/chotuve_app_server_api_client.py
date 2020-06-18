import requests

from steps.config import CHOTUVE_APP_URL

class ChotuveAppServerApiClient:

    def registrarse(self, email, password):
        return self.post('usuario', {'email': email, 'password': password})

    def iniciar_sesion(self, email, password):
        return self.post('usuario/sesion', {'email': email, 'password': password})

    def mi_perfil(self, context):
        return self.get_con_token('usuario', context)
    
    def reaccionar(self, video, reaccion, context):
        return self.post_con_token(f'video/{video}/reaccion', 
            {"reaccion": reaccion}, context)

    def subir_video(self, video_url, titulo, descripcion, ubicacion, duracion, visibilidad, context):
        body = {
            'url': video_url,
            'titulo': titulo,
            'descripcion': descripcion,
            'ubicacion': ubicacion,
            'duracion': duracion,
            'visibilidad': visibilidad
        }
        
        return self.post_con_token('video', body, context)

    def limpiar_base_de_datos(self):
        return requests.delete(f'{CHOTUVE_APP_URL}/base_de_datos')
    
    def get_videos(self, context):
        return self.get_con_token('video', context)

    def get_video_por_id(self, video_id, context):
        return self.get_con_token(f'/video/{video_id}', context)
    
    def get_mas_videos(self, context):
        params = {'offset': 10, 'cantidad': 10}
        return self.get_con_token('video', context, params)

    def get_con_token(self, url, context, params={}):
        headers = {'Authorization': f'Bearer {context.token}'}
        return requests.get(f'{CHOTUVE_APP_URL}/{url}', headers=headers, params=params)

    def post(self, url, json):
        return requests.post(f'{CHOTUVE_APP_URL}/{url}', json=json)
    
    def post_con_token(self, url, json, context):
        headers = {'Authorization': f'Bearer {context.token}'}
        return requests.post(f'{CHOTUVE_APP_URL}/{url}', json=json, headers=headers)

    def put_con_token(self, url, json, context):
        headers = {'Authorization': f'Bearer {context.token}'}
        return requests.put(f'{CHOTUVE_APP_URL}/{url}', json=json, headers=headers)
