from TOKEN import TOKEN_YA
from TOKEN import TOKEN_VK
from TOKEN import user_id
from Yandex import YandexUploader
from VK import VKPhotoBackuper

token_vk = TOKEN_VK
token_ya = TOKEN_YA

info = VKPhotoBackuper(token_vk, user_id)

info.get_photo_info()
