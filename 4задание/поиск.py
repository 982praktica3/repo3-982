import sqlite3

conn = sqlite3.connect("pr.db")
# conn.row_factory = sqlite3.Row
cursor = conn.cursor()

sql = "SELECT * FROM info WHERE name=?"

cursor.execute(sql, [(input('Введите ФИО: '))])
print(cursor.fetchall())