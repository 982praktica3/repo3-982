def Zad4():
    import sqlite3
    import sozdanie
    import dobavlenie
    import vyvod_tablitsy
    import Vyvod_v_XML
    import udalenie
    import redaktirovanie
    import poisk
    sozdanie.Sozd()
    score = 0
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
            dobavlenie.dobav()
        elif score == 2:
            udalenie.udal()
        elif score == 3:
            redaktirovanie.redak()
        elif score == 4:
            poisk.der()
        elif score == 5:
            vyvod_tablitsy.vyvod_tab()
        elif score == 6:
            Vyvod_v_XML.XML()
        elif score == 7:
            return
        else:
            print("Введите коректный номер")
