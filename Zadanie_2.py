from random import randint
n, m = int(input('Введите размер массива: ')), int(input()) 
a = [[randint(-100, 100) for j in range(m)] for i in range(n)]
for i in range(n):print(a[i])
