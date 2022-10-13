from random import random 
R=int(input("Введите размерность массива:"))
A=[0]*R
for i in range(R):
    A[i]=round(random()*10,1)
print ("Исходный массив:",A)
m=max(A)
for i in range (R):
    if A[i]==m:
        for i in range (i+1,R):
            A[i]=0
print("Результат:",A)