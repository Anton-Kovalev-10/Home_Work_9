
def main_menu() -> int:
    print('''Главное меню:
    1 - открыть файл
    2 - сохранить файл
    3 - показать контакты
    4 - добавить контакт
    5 - изменить контакт
    6 - найти контакт
    7 - удалить контакт''')
    while True:
        choice = input('Выбирете пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)
        else:
            print('Введите число от 1 до 7: ')

def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20} '
                  f'{contact.get("comment"):<20} ')

def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}

def input_index(message: str):
    return int(input(message))

def input_search(message):
    return int(input(message))

def change_contact(book: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'contact': contact.get('contact') if contact.get('contact') else book[index-1].get('contact')}

def delete_contact(message: str):
    phone = input('Введите номер телефона который нужно удалить: ')