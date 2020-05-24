import sqlite3

conn = sqlite3.connect("pr.db")
cursor = conn.cursor()

sql = input('Введите ID объекта для удаления: ')

cursor.execute("DELETE FROM info WHERE id=?", sql)
conn.commit()