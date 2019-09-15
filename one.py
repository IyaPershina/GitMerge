import random

n=int(input("Введите n: "))
a=[]
for i in range(n):
    a.append(random.randint(-10,10))

print(a)