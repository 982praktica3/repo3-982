import sqlite3


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
    cursor.execute('''INSERT INTO info(name, date, mobil, toils, address) VALUES (?, ?, ?, ?, ?)''',
                   (name, date, mobil, toils, address))
    # Сохраняем изменения
    conn.commit()
    cursor.close()
    conn.close()
    print('Объект добавлен')
    return
