import sqlite3

def der():
    
 conn = sqlite3.connect("pr.db")

 cursor = conn.cursor()

 sql = "SELECT * FROM info WHERE name=?"

 cursor.execute(sql, [(input('Введите ФИО: '))])
 print(cursor.fetchall())
 return
 
 
def vyvod_tab():
 con = sqlite3.connect('pr.db')
 cursorObj = con.cursor()
 cursorObj.execute('SELECT * FROM info')
 rows = cursorObj.fetchall()
 for row in rows:
  print(row)
 return
 
 
def udal():
 conn = sqlite3.connect("pr.db")
 cursor = conn.cursor()
 sql = input('Введите ID объекта для удаления: ')
 cursor.execute("DELETE FROM info WHERE id=?", sql)
 conn.commit()
 return
 
 
def dobav():
 conn = sqlite3.connect("pr.db")
 cursor = conn.cursor()
    # Вводим данные
 name = input('ФИО: ')
 date = input('Дата рождения: ')
 mobil = input('Номер мобильного: ')
 toils = input('Соц. сети: ')
 address = input('Адрес: ')
    # Вставляем данные в таблицу
 cursor.execute('''INSERT INTO info(name, date, mobil, toils, address) VALUES (?, ?, ?, ?, ?)''', (name, date, mobil, toils, address))
    # Сохраняем изменения
 conn.commit()
 cursor.close()
 conn.close()
 print('Объект добавлен')
 return
 
 
def redak():
 conn = sqlite3.connect("pr.db")
 score=0
 while score != 6:
  print('---------------------------------------')
  print('|1. Изменить ФИО                      |')
  print('|2. Изменить дату рождения            |')
  print('|3. Изменить мобильный                |')
  print('|4. Изменить Соц. сети                |')
  print('|5. Изменить адрес                    |')
  print('|6. Выход                             |')
  score = int(input('|Введите номер необходимого пункта: '))
  if score == 1:
      uId = input('Введите id: ')
      uName = input('Введите ФИО: ')
      with conn:
          cur = conn.cursor()
          cur.execute("UPDATE info SET name=? WHERE id=?", (uName, uId))
          conn.commit()
  elif score == 2:
      uId = input('Введите id: ')
      uDate = input('Введите дату рождения: ')
      with conn:
          cur = conn.cursor()
          cur.execute("UPDATE info SET date=? WHERE id=?", (uDate, uId))
          conn.commit()
  elif score == 3:
      uId = input('Введите id: ')
      uMob = input('Введите мобильный: ')
      with conn:
          cur = conn.cursor()
          cur.execute("UPDATE info SET mobil=? WHERE id=?", (uMob, uId))
          conn.commit()
  elif score == 4:
      uId = input('Введите id: ')
      uToils = input('Введите соц. сеть: ')
      with conn:
          cur = conn.cursor()
          cur.execute("UPDATE info SET toils=? WHERE id=?", (uToils, uId))
          conn.commit()
  elif score == 5:
      uId = input('Введите id: ')
      uAddress = input('Введите адрес: ')
      with conn:
          cur = conn.cursor()
          cur.execute("UPDATE info SET address=? WHERE id=?", (uAddress, uId))
          conn.commit()
 return 
 

def XML():
 import xml.etree.ElementTree as ET
 con = sqlite3.connect('pr.db')
 con = sqlite3.connect('pr.db')
 items = ET.Element("items")
 def sql_fetch(con):
  a=0
  cursor = con.cursor()
  cursor.execute('SELECT * FROM info')
  rows = cursor.fetchall()
  for row in rows:
   a=a+1
   b=str(a)
   n = ET.SubElement(items, "\n")
   row = ET.SubElement(items, "row")
   n = ET.SubElement(row, "\n")
   kd = ET.SubElement(row, "  id")
   n = ET.SubElement(row, "\n")
   name = ET.SubElement(row, "  name")
   n = ET.SubElement(row, "\n")
   date = ET.SubElement(row, "  date")
   n = ET.SubElement(row, "\n")
   mobil = ET.SubElement(row, "  mobil")
   n = ET.SubElement(row, "\n")
   toils = ET.SubElement(row, "  toils")
   n = ET.SubElement(row, "\n")
   address = ET.SubElement(row, "  address")
   n = ET.SubElement(row, "\n")
   n = ET.SubElement(items, "\n")

   cursor.execute("SELECT id FROM info WHERE id=?", b)
   r = ET.SubElement(kd, str(cursor.fetchall()))
   cursor.execute("SELECT name FROM info WHERE id=?", b)
   t = ET.SubElement(name, str(cursor.fetchall()))
   cursor.execute("SELECT date FROM info WHERE id=?", b)
   y = ET.SubElement(date, str(cursor.fetchall()))
   cursor.execute("SELECT mobil FROM info WHERE id=?", b)
   u = ET.SubElement(mobil, str(cursor.fetchall()))
   cursor.execute("SELECT toils FROM info WHERE id=?", b)
   i = ET.SubElement(toils, str(cursor.fetchall()))
   cursor.execute("SELECT address FROM info WHERE id=?", b)
   o = ET.SubElement(address, str(cursor.fetchall()))

  tree = ET.ElementTree(items)
  tree.write("bd.xml", encoding='UTF-8', xml_declaration=True)
 sql_fetch(con)
 return


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


def Zad4():
 score=0
 Sozd()    
 while score != 7:
  print('---------------------------------------')
  print('|1. Добавление строки                 |')
  print('|2. Удаление строки                   |')
  print('|3. Редактирование строки             |')
  print('|4. Поиск                             |')
  print('|5. Вывод таблицы                     |')
  print('|6. Вывод в XML                       |')
  print('|7. Выход                             |')
  score = int(input('|Введите номер необходимого пункта: '))
  if score == 1:
   dobav()
  elif score == 2:
   udal()
  elif score == 3:
   redak()
  elif score == 4:
   der()
  elif score == 5:
   vyvod_tab()
  elif score == 6:
   XML()
  elif score == 7:
   return
  else:
   print("Введите коректный номер")

def Zad1():
 print("Введите числа, из которых будет найден минимум")
 A = [int(el) for el in input().split()]
 print(min(A))
 return
 
def Zad2():
 from random import randint
 n, m = int(input('Введите размер массива: ')), int(input()) 
 a = [[randint(-100, 100) for j in range(m)] for i in range(n)]
 for i in range(n):print(a[i])
 return
 
def Zad3():
 ms1 = list()
 n = int(input("Введите число элементов массива№1: "))
 for i in range(n):
  a = int(input("Введите элемент: "))
  ms1.append(a)
 ms2 = list()
 n = int(input("Введите число элементов массива№2: "))
 for i in range(n):
  a = int(input("Введите элемент: "))
  ms2.append(a)
 ms3 = ms1+ms2
 for i in range(len(ms3)):
  j = i + 1
  for j in range(len(ms3)):
   if ms3[i] < ms3[j]:
    temp = ms3[i]
    ms3[i] = ms3[j]
    ms3[j] = temp
 print(ms3)
 return

fas=0   
while fas != 5:
 print('---------------------------------------')
 fas = int(input('Введите номер задания(5-выход): '))
 if fas == 1:
  Zad1()
 elif fas == 2:
  Zad2()
 elif fas == 3:
  Zad3()
 elif fas == 4:
  Zad4()
 elif fas == 5:
  print('-----------| До свидания |-------------')
 else:
  print("Введите коректный номер")