# -*- coding: utf-8 -*-
"""
Questão 4 (sem usar o sum() )

Alunos: Eric e Rafaela
"""


inteiros = []
soma = 0

for i in range(3):
    linha = []
    cont = 0
    for j in range(3):
        x = int(input(f'Entre com os inteiros da linha {i}: '))
        linha.append(x)
        cont += x
        
    if soma < cont:
        soma = cont
        linha_maior_soma = i
        
    inteiros.append(linha)
      
print(f'A linha de maior soma é a linha {linha_maior_soma}: {inteiros[linha_maior_soma]}')
print(f'A soma do seus termos é {soma}')