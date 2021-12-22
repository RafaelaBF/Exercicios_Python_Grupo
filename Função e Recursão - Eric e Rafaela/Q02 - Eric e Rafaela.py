# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric

Questão 02

Faça um programa, utilizando recursão, que leia um vetor de 1000 números inteiros 
e em seguida informe a quantidade de cada número que foi digitado nesse vetor. 
(Não utilize estrutura de repetição, sob pena de anular a questão).
"""

def leiaVetor(v, vetor):
    if len(vetor) < v:
        vetor.append(int(input("Entre com um número inteiro: ")))
        leiaVetor(v, vetor)
    else:
        return vetor

def contar(vetor, i):
    v = len(vetor)
    if v > i:
        qtd = vetor.count(vetor[i])
        print(f"O numero {vetor[i]} aparece {qtd}")
        deletar(vetor, vetor[i], qtd)
        contar(vetor, i)

        
def deletar(vetor, num, qtd):
    if qtd > 0:   
        vetor.remove(num)
        qtd = qtd - 1
        deletar(vetor, num, qtd)
    else:
        return vetor


i = 0
v = 1000
vetor = []
leiaVetor(v, vetor)
contar(vetor, i)


