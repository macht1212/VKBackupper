from TOKEN import TOKEN_YA
from TOKEN import TOKEN_VK
from TOKEN import user_id
from Yandex import YandexUploader
from VK import VKPhotoBackuper
from pprint import pprint

token_vk = TOKEN_VK
token_ya = TOKEN_YA

# info = VKPhotoBackuper(token_vk, user_id)
#
# pprint(info.save_info())

info = YandexUploader(TOKEN_YA)
pprint(info.get_photos_links_from_vk())
