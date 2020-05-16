from random import randint
n, m = int(input()), int(input()) 
a = [[randint(-100, 100) for j in range(m)] for i in range(n)]
for i in range(n):print(a[i])
