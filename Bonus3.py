#Найти количество элементов в заданном массиве А, отличающихся от минимального на Delta
from random import random
R=int(input("Введите размерность массива:"))
delta= float(input("Введите delta:"))
A=[0]*R
for i in range(R):
    A[i]=round(random()*10,1)
print ("Исходный массив:",A)
m=min(A)
n=0
for i in range (R):
    if A[i]-min(A)==delta:
        n+=1
print("Количество элементов отличающихся от минимального элемента на delta:")
print (n)