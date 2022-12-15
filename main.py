from TOKEN import TOKEN_YA
from TOKEN import TOKEN_VK
from Yandex import YandexUploader

token_vk = TOKEN_VK
token_ya = TOKEN_YA

info = YandexUploader(TOKEN_YA)
info.new_folder('pics from VK')
info.upload('pics from VK')
