import time as t
import random as r
    # Менеджер паролей #

# Заголовки паролей
passwords_names = []

# Сами пароли
passwords = []

    # Функция для добавления пароля

def add_password():
    print('Напишите заголовок для пароля')
    up_name_password = input('>>> ')
    
    print('Напишите ваш пароль')
    new_password = input('>>> ')

    for i in range(len(passwords_names)):
            if up_name_password == passwords_names[i]:
                print('Такое имя уже есть, оно под номером', i+1, ', оно принадлежит паролю', passwords[i])
                break
    for i in range(len(passwords)):
            if new_password == passwords[i]:
                print('Такой пароль уже есть, он под номером', i+1, ', по имени', passwords_names[i])
                break
    passwords_names.append(up_name_password)
    passwords.append(new_password)
    print('Пароль успешно добавлен в менеджер')

    # Функция длоя удаления пароля

def delete_password():
    print('Как вы хотите удалить пароль?')
    t.sleep(0.5)
    print('1 - по названию')
    t.sleep(0.5)
    print('2 - по самому паролю')
    t.sleep(0.5)
    var_for_delete = input('>>> ')
    if var_for_delete == '1':
        print('Введите название пароля')
        password_name_for_delete = input('>>> ')
        
        for i in range(len(passwords_names)):
            if passwords_names[i] == password_name_for_delete:
                passwords_names.remove(password_name_for_delete)
                is_find_on_name_del = True
        if is_find_on_name_del == False:
            print('Не нашли такого пароля')
            t.sleep(0.5)
            print('Возможно у вас еще не добавлено ни одного пароля,')
            print('или не создан с таким именем.')
        else:
            t.sleep(0.5)
            print('Пароль успешно удален')
    elif var_for_delete == '2':
        print('Введите пароль для удаления его')
        t.sleep(0.5)
        password_for_delete = input('>>> ')
        for i in range(len(passwords)):
            if passwords[i] == password_for_delete:
                passwords.remove(password_for_delete)
                is_find_on_pas_del = True
        if is_find_on_pas_del == False:
            print('Не нашли такого пароля')
            t.sleep(0.5)
            print('Возможно у вас еще не добавлено ни одного пароля,')
            print('или не создан с таким значением.')
        else:
            t.sleep(0.5)
            print('Пароль успешно удален')
    else:
        t.sleep(0.5)
        print('Неверная команда')

    # Функция для нахождения пароля по его заголовку

def find_password():
    print('Введите имя вашего пароля')
    find_name = input('>>> ')
    for i in range(len(passwords_names)):
        if passwords_names[i] == find_name:
            print('Вот :)')
            t.sleep(0.5)
            print('Заголовок: ', passwords_names[i])
            t.sleep(0.5)
            print('Пароль: ', passwords[i])
        else:
            t.sleep(0.5)
            print('Мы не нашли такого вароля')

# НАЧАЛО ТОГО ЧТО ВИДИТ ПОЛЬЗОВАТЕЛЬ #

print('------------------------------------------------')
print('---------------Менеджер-Паролей-----------------')
print('------------------------------------------------')
t.sleep(0.5)
while True:
    t.sleep(0.5)
    print('Выбери команду:')
    t.sleep(0.5)
    print('1 --> Добавить пароль')
    t.sleep(0.5)
    print('2 --> Удалить пароль')
    t.sleep(0.5)
    print('3 --> Найти пароль')
    t.sleep(0.5)
    command = int(input('>>> '))
    if command == 1:
        t.sleep(0.5)
        add_password()
    elif command == 2:
        t.sleep(0.5)
        delete_password()
    elif command == 3:
        t.sleep(0.5)
        find_password()
    else:
        t.sleep(0.5)
        print('Неизвестная команда')
    
    