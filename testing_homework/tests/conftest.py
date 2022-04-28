# Добавлен конфиг, т.к иначе при выводе русского текста pytest выводит символы юникода
def pytest_make_parametrize_id(config, val):
    return repr(val)
