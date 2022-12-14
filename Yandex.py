import requests
from VK import VKPhotoBackuper
from TOKEN import TOKEN_VK
from TOKEN import user_id


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

    def get_photos_links_from_vk(self):
        photo = VKPhotoBackuper(TOKEN_VK, user_id)
        photo_links = photo.get_photo_info()
        return photo_links

    def upload(self, path_to_file):
        pass

