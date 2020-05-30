import sqlite3
def der():
    
 conn = sqlite3.connect("pr.db")

 cursor = conn.cursor()

 sql = "SELECT * FROM info WHERE name=?"

 cursor.execute(sql, [(input('Введите ФИО: '))])
 print(cursor.fetchall())
 return