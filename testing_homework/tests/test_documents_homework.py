import pytest
from testing_homework.old_homework_docs import get_name, get_directories, get_list, create_new_shelf, docs_add


@pytest.mark.parametrize("_input, expected", [('11-2', 'Геннадий Покемонов'), ('10006', 'Аристарх Павлов'),
                                              ('12345', 'Ошибка! Людей с таким номером документа нет'),
                                              ('odin_dva', 'Ошибка! Людей с таким номером документа нет')])
def test_get_name(monkeypatch, _input, expected):
    # Имитирую ввод с клавиатуры для данных функции
    monkeypatch.setattr('builtins.input', lambda _: _input)
    result = get_name()
    assert result == expected


@pytest.mark.parametrize("_input, expected", [('11-2', '1'), ('10006', '2'),
                                              ('2207 876234', '1'),
                                              ('12345', 'Ошибка! Несуществующий документ'),
                                              ('odin_dva', 'Ошибка! Несуществующий документ')])
def test_get_directories(monkeypatch, _input, expected):
    monkeypatch.setattr('builtins.input', lambda _: _input)
    result = get_directories()
    assert result == expected


def test_get_list():
    assert get_list() == ['passport 2207 876234 Василий Гупкин', 'invoice 11-2 Геннадий Покемонов',
                          'insurance 10006 Аристарх Павлов']


@pytest.mark.parametrize("name, expected", [('1', 'Такая полка уже существует'),
                                            ('2', 'Такая полка уже существует'),
                                            ('10', 'Полка успешно создана'),
                                            ('best_clients', 'Полка успешно создана')])
def test_create_new_shelf(name, expected):
    assert create_new_shelf(name) == expected


@pytest.mark.parametrize("_list, expected", [(['9915', 'passport', 'Mikhail', '3'], 'Список документов обновлен!'),
                                             (['133', 'insurance', 'Alex', '1'], 'Список документов обновлен!'),
                                             (['366', 'invoice', 'Andrew', '6'], 'Добавлена новая полка, список '
                                                                                 'документов обновлен')])
def test_docs_add(monkeypatch, _list, expected):
    inputs = iter(_list)
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    result = docs_add()
    assert result == expected

