##########################
# Изучаю как работать с sqlite3

import sqlite3

# from logpas import x

base = sqlite3.connect('new.db')
cur = base.cursor()


base.execute('CREATE TABLE IF NOT EXISTS {} (Name PRIMARY KEY, phone, info)'.format('data'))
base.commit()

# text, integer, real, blob, null
cur.execute('INSERT INTO data VALUES(?, ?, ?)', ('Иванов И.И.', '2349834', 'Обычный человек'))
base.commit()
cur.execute('INSERT INTO data VALUES(?, ?, ?)', ('Петров П.В.', '2349834', 'Бычный человек'))
base.commit()
cur.execute('INSERT INTO data VALUES(?, ?, ?)', ('Сидоров С.В.', '2349834', 'Необычный человек'))
base.commit()
# cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
# base.commit()
# r = cur.execute('SELECT * FROM data').fetchall()
# print(r)
# r = cur.execute('SELECT phone FROM data WHERE Name == ?', ('Иванов И.И.',)).fetchone()
# print(r)
# cur.execute('UPDATE data SET info == ? WHERE Name == ?', ('Тот еще гондурас', 'Петров П.В.'))
# base.commit()
# cur.execute('UPDATE data SET phone == ? WHERE phone == ?', ('9886885', '2349834'))
# base.commit()

# cur.execute('DELETE FROM data WHERE Name == ?', ('Сидоров С.В',))
# base.commit()

# cur.execute('DELETE FROM data')
# base.commit()

# base.execute('DROP TABLE IF EXISTS data')
# base.commit()

# base.close()