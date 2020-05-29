import sqlite3

con = sqlite3.connect('pr.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM info')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
