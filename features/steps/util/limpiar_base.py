'''
Utilidad para vaciar la base de datos de Chotuve entre test y test.
'''

import requests

from .chotuve.config import CHOTUVE_APP_URL

def limpiar_base_de_datos():
    return requests.delete(f'{CHOTUVE_APP_URL}/base_de_datos')