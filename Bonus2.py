#Поменять местами четные элементы массива с нечетными
from random import randint 
A=[0]*9
for i in range(len(A)):
    A[i]=randint(1,10)
print (A)
for i in range (1,len(A),2):
    A[i-1],A[i]=A[i],A[i-1]
print(A)