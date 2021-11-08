# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric
"""
'''
Questão 3: 
Faça um programa que leia um número inteiro n qualquer 
e mostre na tela a figura abaixo. 
Ex.: 
Se n = 5 
*        * 
**      ** 
***    *** 
****  **** 
********** 
****  **** 
***    *** 
**      ** 
*        *
'''
n = int(input("Entre com um número: "))
i = 1
x = n*2
while (i < n):
    x-=2
    print('*'*i, ' '*(x-2), '*'*i)
    i+=1
print('*'*n*2)
i-=1
x=2
while (i >= 1):
    print(f"{'*'*i}{' '*x}{'*'*i}")
    i-=1
    x+=2