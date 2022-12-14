import requests
# from main import *
import time
from pprint import pprint


class VKPhotoBackuper:
    HOST = 'https://api.vk.com/method/'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_info(self):
        uri = 'users.get'
        url = self.HOST + uri
        params = {'access_token': self.token,
                  'user_id': self.user_id,
                  'v': 5.131}
        response = requests.get(url, params=params)

        pprint(response.json())

    def get_photo_info(self):
        uri = 'photos.get'
        url = self.HOST + uri
        urls_info = {}

        params = {
            'access_token': self.token,
            'owner_id': self.user_id,
            'album_id': 'profile',
            'count': 5,
            'v': 5.131,
            'extended': 1
        }

        response = requests.get(url, params=params).json()
        response = response['response']['items']

        for i, elem in enumerate(response):
            for j, el in enumerate(response[i]['sizes']):
                if response[i]['sizes'][j]['type'] == 'z':
                    
                elif response[i]['sizes'][j]['type'] == 'y':

        pprint(response)
        pprint(urls_info)
