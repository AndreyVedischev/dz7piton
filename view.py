import sqlite3

def add_contact():
    name = input('Введите имя контакта: ')
    about = input('Введите описание контакта: ')
    number = input('Введите номер контакта: ')
    col = name + ', ' + about + ', ' + number + ';'
    return col

def find_contact():
    name = input('Введите имя контакта: ')
    return name

def action():
    act = input('Введите действие: ')
    return act


# def path_file():
#     path = input('Введите путь: ')
#     return path

###################################

# def path_file():
#     base = sqlite3.connect('new.db')
#     base.execute('CREATE TABLE IF NOT EXISTS {} (Name PRIMARY KEY, phone, info)'.format('data'))
#     base.commit()
#     path = 'new.db'
#     return path