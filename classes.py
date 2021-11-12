import sqluse
import sqlite3 as sl


con = sl.connect('my-test.db')

class note:
    def __init__(self, id, name, id_group, content):
        self.id = id
        self.name = name
        self.id_group = id_group
        self.content = content

class group:
    def __init__(self, id, group_name):
        self.id = id
        self.group_name = group_name

class text:
    def __init__(self, id, text, id_note, pos_x, pos_y):
        self.id = id
        self.text = text
        self.id_note = id_note
        self.pos_x = pos_x
        self.pos_y = pos_y


def notecreate(id):
    tabl = sqluse.sql_read(con, "Notes", id)
    a = note(tabl[0][0], tabl[0][1], tabl[0][2], tabl[0][3])
    return a


print(notecreate("1"))

