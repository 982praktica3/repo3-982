# 1 массив
ms1 = list()
n = int(input("Введите число элементов массива№1: "))
# Цикл для записи элементов в список.
for i in range(n):
    # Запись в массив
    a = int(input("Введите элемент: "))
    ms1.append(a)
# 2 массив
ms2 = list()
n = int(input("Введите число элементов массива№2: "))
# Цикл для записи элементов в список.
for i in range(n):
    # Запись в массив
    a = int(input("Введите элемент: "))
    ms2.append(a)
ms3 = ms1+ms2
# Сортировка
for i in range(len(ms3)):
    j = i + 1
    for j in range(len(ms3)):
        if ms3[i] < ms3[j]:
            temp = ms3[i]
            ms3[i] = ms3[j]
            ms3[j] = temp
print(ms3)
