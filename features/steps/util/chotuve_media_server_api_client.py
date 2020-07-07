import requests

from util.chotuve.config import CHOTUVE_MEDIA_URL

class ChotuveMediaServerApiClient:

    def get_videos(self):
        param = {'solo_habilitados': 'false'}
        return requests.get(f'{CHOTUVE_MEDIA_URL}/video', params = param)

    def deshabilitar_video(self, video_id):
        return requests.put(f'{CHOTUVE_MEDIA_URL}/video/{video_id}', json = {'habilitado': False})

    def habilitar_video(self, video_id):
        return requests.put(f'{CHOTUVE_MEDIA_URL}/video/{video_id}', json = {'habilitado': True})