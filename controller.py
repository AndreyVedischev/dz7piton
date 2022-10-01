import view
import tdb_function
import sqlite3

# def button_click():
#     p = 'data.txt'
#     act = view.action()
#     match act:
#         case '/r':
#             tdb_function.read_file(p)
#         case '/w':
#             tdb_function.write_in_file(p)
#         case '/f':
#             tdb_function.find_in_file(p)
#         case '/d':
#             tdb_function.delete_in_file(p)

##########################################


def button_click():
    p = sqlite3.connect('new.db')
    
    act = view.action()
    match act:
        case '/r':
            tdb_function.read_file(p)
        case '/w':
            tdb_function.write_in_file(p)
        case '/f':
            tdb_function.find_in_file(p)
        case '/d':
            tdb_function.delete_in_file(p)
    