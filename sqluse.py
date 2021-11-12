import sqlite3 as sl

con = sl.connect('my-test.db')


def sql_insert(base, data, tabl):
    sql = 'INSERT INTO ' + tabl + ' (id, name, id_group, content) values(?, ?, ?, ?)'

    with base:
        base.executemany(sql, data)


def sql_read(base, tabl, id):
    table = []
    with con:
        data = con.execute("SELECT * FROM " + tabl + " where id=" + id)
        for row in data:
            table.append(row)
    return table

def sql_read_all_notes(base, id_group):
    table = []
    with con:
        data = con.execute("SELECT notes.id, notes.name, groups.name FROM notes, groups where notes.id_group = groups.id and id_group = " + id_group)
        for row in data:
            table.append(row)
    return table


def sql_remove(base, tabl, id):
    base.execute("DELETE from " + tabl + " where id=" + id)



