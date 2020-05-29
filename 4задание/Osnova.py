score=0
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
    import dobavlenie
 elif score == 2:
    import udalenie
 elif score == 3:
    import redaktirovanie
 elif score == 4:
    import poisk
 elif score == 5:
     import vyvod_tablitsy
 elif score == 6:
     import Vyvod_v_XML
 elif score == 7:
     print('-----------| До свидания |-------------')
 else:
     print("Введите коректный номер")



