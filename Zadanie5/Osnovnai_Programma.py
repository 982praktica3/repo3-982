import Zadanie_1
import Zadanie_2
import Zadanie_3
import Zadanie_4
fas=0   
while fas != 5:
 print('---------------------------------------')
 fas = int(input('Введите номер задания(5-выход): '))
 if fas == 1:
  Zadanie_1.Zad1()
 elif fas == 2:
  Zadanie_2.Zad2()
 elif fas == 3:
  Zadanie_3.Zad3()
 elif fas == 4:
  Zadanie_4.Zad4()
 elif fas == 5:
  print('-----------| До свидания |-------------')
 else:
  print("Введите коректный номер")