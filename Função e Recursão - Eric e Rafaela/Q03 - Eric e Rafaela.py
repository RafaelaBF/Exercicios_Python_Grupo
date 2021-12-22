# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric

Questão 03

Faça um programa, utilizando recursão, que leia um vetor de 100 números inteiros, 
e em seguida os ordene em ordem decrescente de valor. 
(Não utilize estrutura de repetição, sob pena de anular a questão).
"""

def leiaVetor(v, vetor):
    if len(vetor) < v:
        vetor.append(int(input("Entre com um número inteiro: ")))
        leiaVetor(v, vetor)
    else:
        return vetor


def troca(lis, i, j):
    tmp = lis[i]   
    lis[i] = lis[j]
    lis[j] = tmp

def busca(i, j, lis):
    if j < i:
        if lis[j] > lis[i-1]:
              troca(lis, j, i-1)
        j += 1
        bolha(lis, i, j) 
    else:
        j = 0
        i = i - 1
        bolha(lis, i, j) 

    
def bolha(lis, i, j):
    if i > 0:
        busca(i, j, lis)
    else:
        print(lis)
        return lis        
    
j = 0  
v = 5
vetor = []

leiaVetor(v, vetor)
bolha(vetor, v, j)


