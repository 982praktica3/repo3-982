import sqlite3
conn = sqlite3.connect("pr.db")
uId = input('id')
stolb = input('столбец')
uPrice = input('имя')
with conn:
    cur = conn.cursor()
    cur.execute("UPDATE info SET ?  =  ? WHERE id=?", (uPrice, uId))
    conn.commit()
print ("Строк изменено: %d" % cur.rowcount)