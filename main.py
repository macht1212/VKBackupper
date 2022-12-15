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
# photo = VKPhotoBackuper(token_vk, user_id)
# photo.get_photo_info()


info = YandexUploader(TOKEN_YA)
info.new_folder('pics from VK')
info.upload('pics from VK')
