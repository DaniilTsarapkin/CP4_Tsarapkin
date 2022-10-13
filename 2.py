from os import remove
from random import random 
R=int(input("Введите размерность массива A:"))
F=int(input("Введите размерность массива B:"))
A=[0]*R
B=[0]*F
C=[0]*max(R,F)
for i in range(R):
    A[i]=round(random()*10,1)
print ("Mассив A:")
print (A)
for i in range(F):
    B[i]=round(random()*10,1)
print ("Mассив B:")
print (B) 
N=0
for i in range (len(A)):
    for j in range (len(B)):
        if A[i]==B[j]:
            C[N]=A[i]
            N+=1
print ("Совпадающие элементы (0 не является совпадающим элементом):")
for N in range (len(C)):
    print (C[N])