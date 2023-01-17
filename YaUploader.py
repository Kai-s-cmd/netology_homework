import os
import requests
from pprint import pprint
from token_yandex import TOKEN


class YaUploader:
    link_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self):
        self.token = token

    @property
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, file_path):
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.link_for_upload, params=params,
                                headers=self.headers)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        href = self.get_upload_link(file_path).get('href')
        if not href:
            return

        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print('Файл загружен')
                return True
            print('Файл не загружен.', response.status_code)
            return False


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'superhero_api.py'
    token = TOKEN
    uploader = YaUploader()
    result = uploader.upload(os.path.join(path_to_file))
