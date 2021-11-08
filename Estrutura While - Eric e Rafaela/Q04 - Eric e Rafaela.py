# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric
"""
'''
Questão 4:
Faça um programa que leia um número inteiro positivo 
e em seguida monte a figura abaixo.  (Não utilize vetor) 
Exemplo: 
Se o número digitado for n=0. Deverá aparecer na tela: 
* 
Se o número digitado for n=1. Deverá aparecer na tela: 
* 
* 
Se o número digitado for n=2. Deverá aparecer na tela: 
** 
* 
* 
Se o número digitado for n=3. Deverá aparecer na tela: 
******
**
*
*
Se o número digitado for n=4. Deverá aparecer na tela: 
************************************************************************************************************************
******
**
*
*
'''
n = int(input("Entre com um número: "))
n1 = 1
n2 = 1
i = 0
while (i < n+1):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    i += 1
maior = n2-n1
auxmaior = n1-maior
i=0
while (i < n+1):
    x = maior
    fat = 1
    while (x > 1):
        fat*=x
        x-=1
    print("*" * fat)
    y = maior
    maior = auxmaior
    auxmaior = y-auxmaior
    i+=1