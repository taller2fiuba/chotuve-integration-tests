import os

def raise_value_error(message):
    '''
    Lanza una excepción de tipo ValueError con el mensaje indicado.
    '''
    raise ValueError(message)

CHOTUVE_APP_URL=os.environ.get('CHOTUVE_APP_URL') or raise_value_error('Falta la variable de entorno CHOTUVE_APP_URL')
CHOTUVE_MEDIA_URL=os.environ.get('CHOTUVE_MEDIA_URL') or raise_value_error('Falta la variable de entorno CHOTUVE_MEDIA_URL')
CHOTUVE_AUTH_URL=os.environ.get('CHOTUVE_AUTH_URL') or raise_value_error('Falta la variable de entorno CHOTUVE_AUTH_URL')

