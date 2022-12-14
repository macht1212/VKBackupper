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
        urls_info = []

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

        photo_data = {}

        for elem in response:

            res = elem['sizes']
            max_size = 0
            max_size_url = ''

            for size in res:
                if size['height'] >= max_size:
                    max_size = size['height']
                    max_size_url = size['url']
            if f"{elem['likes']['count']}.jpg" in photo_data.keys():
                photo_data[f"{elem['likes']['count']}+{elem['date']}.jpg"] = max_size_url
            else:
                photo_data[f"{elem['likes']['count']}.jpg"] = max_size_url

        pprint(photo_data)
