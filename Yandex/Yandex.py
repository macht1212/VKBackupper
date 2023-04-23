import os
import requests
from VK.VK import VKPhotoBackuper

from dotenv import load_dotenv

load_dotenv()

TOKEN_VK = os.getenv('TOKEN_VK')
user_id = os.getenv('USER_ID')


class YandexUploader:
    HOST = 'https://cloud-api.yandex.net:443'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self, path_to_file):
        uri = '/v1/disk/resources/upload'
        url = self.HOST + uri
        params = {'path': path_to_file}
        response = requests.get(url=url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def new_folder(self, folder_name):
        uri = '/v1/disk/resources/'
        url = self.HOST + uri

        params = {
            'path': f'{folder_name}',
            'overwrite': 'false'
        }

        response = requests.put(url=url, headers=self.get_headers(), params=params)
        return response.status_code

    def upload(self, folder):
        photo = VKPhotoBackuper(TOKEN_VK, user_id)
        photo_links = photo.get_photo_info()

        uri = '/v1/disk/resources/upload'
        url = self.HOST + uri

        for key, value in photo_links.items():
            file_name = key
            url_link = value[0]

            path_to_file = f'/{folder}/{file_name}'

            params = {
                'path': path_to_file,
                'url': url_link,
                'overwrite': 'true'
            }

            response = requests.post(url=url, headers=self.get_headers(), params=params)

            print(response.status_code)
