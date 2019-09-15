import random

n=int(input("Введите n: "))
a=[]
for i in range(n):
    a.append(random.randint(-10,10))

print(a)

neg=[]
zero=[]
pos=[]

for el in a:
    if el<0:
        neg.append(el)
    if el==0:
        zero.append(el)
    if el>0:
        pos.append(el)

print("Отрицательные")
print(neg)
print("Нули")
print(zero)
print("Положительные")
print(pos)