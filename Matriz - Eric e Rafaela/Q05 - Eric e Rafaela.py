# -*- coding: utf-8 -*-
"""
Questão 5

Alunos: Eric e Rafaela
"""

A = []
num_col_lin = int(input('Entre com o número de linhas e colunas: '))

for i in range(num_col_lin):
    linha = []
    for j in range(num_col_lin):
        linha.append(int(input('Entre com um número: ')))
        
    A.append(linha)
    
    
AT = [0]*len(A[0])

for i in range(len(A)):
    AT[i] = [0]*len(A)
    for j in range(len(A[i])):
        AT[i][j] = A[j][i]

print('A matriz transposta  é: ')        
print(AT)
        



