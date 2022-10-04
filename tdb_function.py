
import view
import sqlite3



# def read_file(path : str):
#     path = 'data.txt'
#     with open(path,encoding = 'utf-8', mode = 'r') as file:
#         print(file.read())

# def write_in_file(path : str):
#     path = 'data.txt'
#     with open(path,encoding = 'utf-8', mode = 'a') as file:
#         file.write(f'{view.add_contact()}\n')

# def find_in_file(path : str):
#     path = 'data.txt'
#     with open(path,encoding = 'utf-8', mode = 'r') as file:
#         f = file.read().split(';')
#         f_name = view.find_contact()
#         for i in f:
#             if f_name in i:
#                 print(i)
#         else:
#             print('Контакт не найден')

# def delete_in_file(path : str):
#     path = 'data.txt'
#     with open(path,encoding = 'utf-8', mode = 'r+') as file:
#         f = file.read()
#         f = f.split(';')
#         f_name = view.find_contact()
#         for i in f:
#             if f_name in i:
#                     f.remove(i)
#                     break
#         else:
#             print('Контакт не найден')
#     with open(path,encoding = 'utf-8', mode = 'w') as file:
#         file.write(';'.join(f))
                    
################################
# попытка представить работу с файлами базы cqlite

def read_file(base):
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    r = cur.execute('SELECT * FROM data').fetchall()
    print(r)


def find_in_file(base):
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    r = cur.execute('SELECT phone FROM data WHERE Name == ?', (view.find_contact(),)).fetchone()
    
    print(r)


def write_in_file(base):
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    cur.execute('INSERT INTO data (Name, phone, info) VALUES (?,?,?)', (view.add_contact(), ))
    base.commit()
    base.close()


def delete_in_file(base):
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    cur.execute('DELETE FROM data WHERE Name == ?', (view.find_contact(),))
    base.commit()
    base.close()