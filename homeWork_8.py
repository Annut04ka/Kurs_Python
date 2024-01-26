# ДОБАВЛЕНА новая функциЯ copy_data в  программу для копирования данных из одного файла в другой. 
# Пользователь может ввести номер строки, которую необходимо скопировать, и эта строка будет перенесена из файла phone.txt в файл phone_copy.txt.
# Функция copy_data вызывается при выборе пользователем соответствующего пункта меню.     
# ДОБАВЛЕНА новая функциЯ update_data в  программу для изменения данных. 
# ДОБАВЛЕНА новая функциЯ delete_data в  программу для удаления данных. 
import os

def input_data(data):
    while True:
         user_input = input('введите номер телефона: ')
         if not user_input or not user_input.isdigit():
              return data
         if user_input in data:
            print('Такой номер уже есть!')
         else:
             temp = input("ФИО через пробел: ").split()
             if len(temp) != 3:
                 print('Ошибка')
             else:
                 data[user_input] = temp
                 with open('phone.txt', 'a') as f:
                     print(f"{user_input}\t{temp[0]}\t{temp[1]}\t{temp[2]}", file=f)
                 return data


def show_data(data):
    for key, value in data.items():
         print(key, *value)

def search_data(data):
    user_input = input("Поиск 1: номер телефона или 2: иное")
    if user_input not in {'1', '2'}:
         return
    if user_input == '1':
         phone = input("введите номер телефона: ")
         print(data.get(phone, 'Нет номера'))
         return
    other = input("Имя или Фамилия или Отчество")
    if ' ' in other or not other:
        print('Ошибка')
        return
    for key, values in data.items():
         for value in values:
             if other in value:
                 print(key, *values)
                 break
# при каждом запуске функции copy_data данные добавляются в конец файла
# Функция copy_data вызывается при выборе пользователем соответствующего пункта меню.            
def copy_data():
    source_file = 'phone.txt'
    target_file = 'phone_copy.txt'
    line_number = int(input("Введите номер строки для копирования: "))
    
    with open(source_file, 'r') as source, open(target_file, 'a') as target:
        for i, line in enumerate(source, start=1):
            if i == line_number:
                target.write(line)
                print(f"Строка {line_number} скопирована в {target_file}")
                break
        else:
            print(f"Строка {line_number} не найдена в {source_file}")
            
# Перезаписываем файл с обновленными данными
def write_data_to_file(data):
    with open('phone.txt', 'w') as f:
        for phone, fio in data.items():
            f.write(f"{phone}\t{fio[0]}\t{fio[1]}\t{fio[2]}\n")

def update_data(data):
    name_or_surname = input("Введите имя или фамилию для изменения данных: ")
    found = False
    for key, values in list(data.items()):
        if name_or_surname in values:
            print(f"Найдена запись: {key}, {values}")
            new_phone = input("Введите новый номер телефона: ")
            # Проверяем, существует ли новый номер телефона в справочнике
            if new_phone in data and new_phone != key:
                print("Такой номер телефона уже существует в справочнике.")
                break
            new_fio = input("Введите новое ФИО через пробел: ").split()
            if len(new_fio) == 3:
                # Удаляем старую запись, если номер телефона изменен
                if new_phone != key:
                    del data[key]
                data[new_phone] = new_fio
                write_data_to_file(data)  # Перезаписываем файл с обновленными данными
                found = True
                print("Данные успешно обновлены.")
                break
            else:
                print("Ошибка ввода ФИО.")
    if not found:
        print("Запись не найдена.")

def delete_data(data):
    name_or_surname = input("Введите имя или фамилию для удаления данных: ")
    found = False
    for key, values in list(data.items()):
        if name_or_surname in values:
            print(f"Найдена запись: {key}, {values}")
            confirm = input("Вы действительно хотите удалить эту запись? (да/нет): ")
            if confirm.lower() == 'да':
                del data[key]
                write_data_to_file(data)  # Перезаписываем файл с обновленными данными
                found = True
                print("Запись успешно удалена.")
                break
    if not found:
        print("Запись не найдена.")           

def main():
    if os.path.exists('phone.txt'):
        with open('phone.txt', 'r+') as file:
             data = {}
             for sentence in file:
                 phone, second_name, first_name, third_name = sentence.split('\t')
                 data[phone] = [second_name, first_name, third_name]
    else:
         with open('phone.txt', 'w') as f:
             data = {}

    print("Добро пожаловать в телефонный справочник")
    while True:
        user_input = input("""1: ввести новые данные \n2: просмотреть данные \n3: поиск \n4: копирование данных \n5: изменить данные \n6: удалить данные \n7: выход\n""")
        if user_input not in {'1', '2', '3', '4', '5', '6', '7'}:
            print('Неверное значение!')
        elif user_input == '1':
            data = input_data(data)
        elif user_input == '2':
            show_data(data)
        elif user_input == '3':
            search_data(data)
        elif user_input == '4':
            copy_data()
        elif user_input == '5':
            update_data(data)
        elif user_input == '6':
            delete_data(data)    
        else:
            print('До свидания!!')
            break

if __name__ == '__main__':
     main()
