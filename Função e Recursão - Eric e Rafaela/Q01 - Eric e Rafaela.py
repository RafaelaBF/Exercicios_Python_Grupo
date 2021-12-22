# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric

Questão 01

Faça  um  programa,  utilizando  recursão,  que  leia  dois  números  binários,  com  qualquer quantidade de bits,
e em seguida efetue a soma desses dois números binários. 
Obs.: Não é para converter os números para decimais 
e realizar a operação de soma.  
Todas as operações devem ser realizadas com números binários.  
(Não utilize estrutura de repetição, sob pena de anular a questão). 
"""

def somaBinario(x, y, w, tam, vetor):
    
    if w == 0:
        if x[tam] == "0" or y[tam] == "0":
            if x[tam] == "0" and y[tam] == "0":
                vetor.append("0") ## 0
                w = 0
            else:
                vetor.append("1") ## 1
                w = 0
        else:
            if tam <= 1:
                vetor.append("10") ## 10
                w = 0
            else:
                w = 1
                vetor.append("0") ## 0
    else:
        if x[tam] == "0" or y[tam] == "0":
            if x[tam] == "0" and y[tam] == "0":
                vetor.append("1") ## 1
                w = 0
            else:
                vetor.append("0")  ## 0
                w = 1
        else:
            if tam <= 1:
                w = 1
                vetor.append("11") ## 11
            else:
                w = 1
                vetor.append("1") ## 1
                
    if tam == 0:
        return vetor
    else:
        return somaBinario(x, y, w, tam-1, vetor)

          
        
num1 = input("Entre com um binário: ")
num2 = input("Entre com outro binário: ")

TamNum = len(num1)
vetor = []
SubiuUm = 0

vetor = somaBinario(num1, num2, SubiuUm, TamNum-1, vetor)
    
print(f"A soma dos binários {num1} e {num2} é: {vetor}")








