import sqlite3

con = sqlite3.connect("pr.db")
cursor = con.cursor()
sql = input('Введите ID объекта для удаления: ')

cursor.execute("DELETE FROM info WHERE id=?", sql)

def sql_fetch(con):
    a = 1
    cursor = con.cursor()
    cursor.execute('SELECT * FROM info')
    rows = cursor.fetchall()
    for row in rows:
        s=str(a)
        a=a+1
        b=str(a)
        cursor.execute("UPDATE info SET id=? WHERE id=?", (s, b)) 
        
sql_fetch(con)        
con.commit()
