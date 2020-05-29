import sqlite3


def der():

    conn = sqlite3.connect("pr.db")
    cursor = conn.cursor()
    n = input('введите имя')
    n = '%' + n + '%'
    sql = "SELECT * FROM info WHERE name LIKE ? "
    cursor.execute(sql, [n])
    print(cursor.fetchall())
    return
