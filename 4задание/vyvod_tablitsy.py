import sqlite3


def vyvod_tab():
    con = sqlite3.connect('pr.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM info')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    return
