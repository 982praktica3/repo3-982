import sqlite3


def redak():
    conn = sqlite3.connect("pr.db")
    score = 0
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
