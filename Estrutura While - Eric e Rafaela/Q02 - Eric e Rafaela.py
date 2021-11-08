# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric
"""
'''
Questão 2: 
Faça um programa que leia um número inteiro n qualquer 
e mostre na tela a figura abaixo. 
Ex.: 
Se n = 5 
    ** 
   **** 
  ****** 
 ******** 
********** 
 ******** 
  ****** 
   **** 
    **

'''
n = int(input("Entre com um número: "))
i = 1
x = n
while (i < n):
    print(' '*(x-1), '*'*(i*2))
    i+=1
    x-=1
while (i >= 1):
        print(' '*(x-1), '*'*i*2)
        i-=1
        x+=1