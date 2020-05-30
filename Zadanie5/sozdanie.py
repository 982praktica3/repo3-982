import sqlite3
def Sozd():
 was=0
 wor=0
 while was != 2:
  print('---------------------------------------')
  was = int(input("У вас создана база данных?(1-да,2-нет,) "))
  if was == 1:
   return
  elif was == 2:
   while wor != 2:
    wor = int(input('Создать базу данных?(1-да,2-нет,) '))
    if wor == 1:
     conn = sqlite3.connect("pr.db")
     cursor = conn.cursor()
     cursor.execute("""CREATE TABLE info
                       (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, date text,
                       mobil text, toils text, address text)
                    """)
     return
    elif wor == 2:
     print("Ой, всё")
     exit()
    else:
     print("Руки не из того места растут")
  else:
   print("Руки не из того места растут")  