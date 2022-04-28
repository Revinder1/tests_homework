import requests



class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
                }

    @staticmethod
    def switcher(arg):
        my_switcher = {
            201: 'Папка успешно создана',
            400: 'Некорректные данные',
            403: 'API недоступно. Ваши файлы занимают больше места, чем у Вас есть',
            404: 'Не удалось найти запрошенный ресурс',
            409: 'Папка с таким именем уже существует, попробуйте изменить путь'
        }
        return my_switcher.get(arg, "nothing")

    def put_directory(self, path):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        response = requests.put(f'{files_url}?path={path}', headers=headers)
        return self.switcher(response.status_code)


if __name__ == '__main__':
    TOKEN = ''
    ya = YaUploader(TOKEN)
    print(ya.put_directory('TEST_FOLDER'))
    print(ya.put_directory('TEST_FOLDER/IN_TEST_FOLDER'))
    # ya.get_disk_info('/')
    # print(ya.is_folder_exists('/', 'TEST_FOLDER'))
