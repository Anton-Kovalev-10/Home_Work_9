import view
import model

def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                pb = model.get_phone_book()
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                contact = view.add_contact()
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта')
                    contact = view.change_contact()
                    model.change_contact(contact, index)
            case 6:
                search = view.input_search('Введите искомый элемент: ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакты не найдены')
            case 7:
                search = view.delete_contact('Введите номер телефона который нужно удалить: ')
                result = model.delete_contact(search)
            case _:
                pass