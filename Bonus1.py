#Найти количетсво элементов массива, которые больше среднего значения
from random import randint 
A=[0]*10
for i in range(len(A)):
    A[i]=randint(1,10)
print (A)
S= sum(A)
Sz= S/len(A)
n=0
for i in range(len(A)):
    if i > Sz:
        n +=1
print (n)