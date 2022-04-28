import pytest
import requests
import mock
from testing_homework.yandex_api_sample import YaUploader




@pytest.mark.parametrize("status_code, expected_result", [(201, 'Папка успешно создана'),
                                                          (400, 'Некорректные данные'),
                                                          (403, 'API недоступно. Ваши файлы занимают больше места, '
                                                                'чем у Вас есть'),
                                                          (404, 'Не удалось найти запрошенный ресурс'),
                                                          [409,
                                                           'Папка с таким именем уже существует, попробуйте изменить '
                                                           'путь']
                                                          ])
@mock.patch("testing_homework.yandex_api_sample.requests.put")
def test_put_directory(mock_requests_put, status_code, expected_result):
    token = ''
    ya = YaUploader(token)
    mock_requests_put.return_value = mock.Mock(status_code=status_code)
    assert ya.put_directory('TEST_FOLDER') == expected_result
