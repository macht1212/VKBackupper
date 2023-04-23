import os
from dotenv import load_dotenv
from Yandex.Yandex import YandexUploader

load_dotenv()

TOKEN_YA = os.getenv('TOKEN_YA')

info = YandexUploader(TOKEN_YA)
info.new_folder('pics from VK')
info.upload('pics from VK')
