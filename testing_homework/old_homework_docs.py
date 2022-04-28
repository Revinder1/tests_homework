documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name():
    """ asking document number and returning name of document owner from list """

    ask = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == ask:
            return doc['name']
    return 'Ошибка! Людей с таким номером документа нет'


def get_directories():
    """ asking document number and returning shelf number with this document """

    ask = input('Введите номер документа: ')
    for key, value in directories.items():
        for number in value:
            if number == ask:
                return key
    return 'Ошибка! Несуществующий документ'


def get_list():
    """ turn documents in list format [x y z] """
    new_list = []
    for dicts in documents:
        new_list.append(' '.join(dicts.values()))
    return new_list


def create_new_shelf(name: str):
    if name not in directories.keys():
        directories[name] = []
        return 'Полка успешно создана'
    return 'Такая полка уже существует'


def docs_add():
    """ adding new documents in catalog and shelf; asking number, type, name and shelf's number """

    ask_doc_number = input('Номер документа, который хотите добавить: ')
    ask_doc_type = input('Введите тип документа: ')
    ask_name = input('Имя владельца документа: ')
    ask_shelf = input('Номер полки, на которой хранится документ: ')
    new_dict = dict()
    new_dict.update({'type': ask_doc_type, 'number': ask_doc_number, 'name': ask_name})
    documents.append(new_dict)
    for key, value in directories.items():
        if key == ask_shelf:
            value.append(ask_doc_number)
            return 'Список документов обновлен!'
    create_new_shelf(ask_shelf)
    directories[ask_shelf].append(ask_doc_number)
    return 'Добавлена новая полка, список документов обновлен'


def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            print(f'Имя человека, которому принадлежит документ: {get_name()}')
        elif user_input == 's':
            print(f'Номер полки, на которой находится документ: {get_directories()}')
        elif user_input == 'l':
            print('Список всех документов: ')
            print(*get_list(), sep='\n')
        elif user_input == 'a':
            print(docs_add())
        elif user_input == 'q':
            print('До свидания!')
            break


if __name__ == '__main__':
    main()
