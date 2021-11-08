# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric
"""
'''
Questão 1: 
Faça um programa que leia um número inteiro n qualquer 
e mostre na tela a figura abaixo. 
Ex.: 
Se n = 5 
* 
** 
*** 
**** 
***** 
**** 
*** 
** 
*
'''

n = int(input("Entre com um número: "))
i = 1
while (i < n):
    print('*'*i)
    i+=1
while (i >= 1):
        print('*'*i)
        i-=1
