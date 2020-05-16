import numpy as np
n = int(input('Введите размер массивов: '))
a = np.random.randint(-50, 50, n)
b = np.random.randint(-50, 50, n)
c = sorted(np.concatenate((a, b)))
print('Изначальные массивы: ', a, ';', b)
print('Отсортированный массив', c)

