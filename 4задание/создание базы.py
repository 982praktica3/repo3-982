import sqlite3

conn = sqlite3.connect("pr.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE info
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, date text,
                  mobil text, toils text, address text)
               """)

