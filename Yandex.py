import requests
from TOKEN import TOKEN_YA
# from TOKEN import TOKEN_VK
# from VK import VKPhotoBackuper


class YandexUploader:
    """This class contain a few methods to get and push necessary information to your oun repository on claud service
    like Yandex.Disc.

    Also class connected with other class which works with VK API.

    """

    HOST = 'https://cloud-api.yandex.net:443'

    def __init__(self, token, name):
        self.token = TOKEN_YA
        self.name = name

    def get_headers(self):
        """
        Method returns headers
        """
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self, path_to_file):
        """
        Method returns response Upload link
        :param path_to_file: name.jpg
        :return: href for uploading
        """
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

    def upload(self, path_to_file):
        """
        Method upload file to Yandex.Disk
        :param path_to_file: name.jpg
        :return: status of transaction: 200, 201 - all was correct, 4** - bad staff
        """
        upload_link = self.get_upload_link(path_to_file)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(self.name, 'rb'))
        print(response.status_code)
