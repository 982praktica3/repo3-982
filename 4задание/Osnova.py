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
    import добавление
 elif score == 2:
    import удаление
 elif score == 3:
    import редактирование
 elif score == 4:
    import поиск
 elif score == 5:
     import вывод_таблицы
 elif score == 6:
     import Вывод_в_XML
 elif score == 7:
     print('-----------| До свидания |-------------')
 else:
     print("Введите коректный номер")



