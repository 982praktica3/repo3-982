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
    ms3 = ms1 + ms2
    for i in range(len(ms3)):
        j = i + 1
        for j in range(len(ms3)):
            if ms3[i] < ms3[j]:
                temp = ms3[i]
                ms3[i] = ms3[j]
                ms3[j] = temp
    print(ms3)
    return
