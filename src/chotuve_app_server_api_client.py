import requests

from config import CHOTUVE_APP_URL

class ChotuveAppServerApiClient:

    def mi_perfil(self, context):
        return self.get_con_token('usuario/perfil', context)

    def get_con_token(self, url, context):
        headers = {'Authorization': f'Bearer {context.token}'}
        return requests.get(f'{CHOTUVE_APP_URL}/{url}', headers=headers)
