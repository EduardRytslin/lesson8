def file_read():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()
    
def file_append(text=""):
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(text)

# Функции ввода
def input_sur():
    return input("Введите Фамилию: ")

def input_name():
    return input("Введите Имя: ")

def input_pat():
    return input("Введите Отчество: ")

def input_phone():
    return input("Введите Телефон: ")

def input_adr():
    return input("Введите Адрес: ")
# Функции ввода

def input_data():
    sur = input_sur()
    name = input_name()
    pat = input_pat()
    phone = input_phone()
    adr = input_adr()

    contact_str = f"{sur} {name} {pat} {phone}\n{adr}\n\n" #Форматирование для записи
    file_append(contact_str)

def print_data():
    print(file_read())

#Поиск
def search_contact():
    print("Возможные варианты поиска:\n"
          "1. По фамилии\n"
          "2. По имени\n"
          "3. По отчеству\n"
          "4. По номеру телефона\n"
          "5. По адресу\n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод, повторите попытку")
        command = input("Выберите вариант поиска: ")

    i_var = int(command) - 1

    search = input("Введите данные для поиска: ")
    print()
    contacts_list = file_read().rstrip().split("\n\n")

    for contact_str in contacts_list:
        cont_list = contact_str.replace("\n"," ").split()
        if search in cont_list[i_var]:
            print(contact_str)
            print()

    cmd = input("Хотите ли вы изменить данные?\n")
    if cmd == "Да":
        print("Что вы хотите изменить?\n"
              "1 — Фамилию\n"
              "2 — Имя\n"
              "3 — Отчество\n"
              "4 — Номер телефона\n"
              "5 — Адрес\n"
              )
        cm = input("Выберите вариант: ")
        contact_str[int(cm)-1] = input("Введите новый атрибут: ")

#Поиск

def u_interface():
    command = ""
    while command != "4":
        print("Меню\n"
            "1. Добавить контакт\n"
            "2. Найти контакт\n"
            "3. Вывести все контакты\n"
            "4. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1","2","3","4"):
            print("Некорректный ввод, повторите попытку")
            command = input("Выберите пункт меню: ")

        print()
        match command:
            case "1":
                input_data()
            case "2":
                search_contact()
            case "3":
                print_data()
            case "4":
                print("Всего хорошего!")


u_interface()