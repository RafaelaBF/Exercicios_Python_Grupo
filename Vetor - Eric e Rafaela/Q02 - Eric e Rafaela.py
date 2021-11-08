# -*- coding: utf-8 -*-
"""
Rafaela e Eric

Questão 2

"""

i = 0
parou = 0

v = [int(y) for y in input('Entre com o vetor v: ').split()]
tam_v = int(input('Entre com o tamanho do vetor v: '))

x = [int(y) for y in input('Entre com o vetor x: ').split()]
tam_x = int(input('Entre com o tamanho do vetor x: '))

if tam_x >= tam_v:
    print(f'O vetor x {x} não é subvetor do vetor v {v}.')
else:
    while i < tam_x:
        cont = v.count(x[i])
        if cont == 0:
            i = tam_x 
            parou = 1
            print(f'O vetor x {x} não é subvetor do vetor v {v}.')
        i += 1
        
    if parou != 1:
        i = 0
        while i < tam_x:
            cont = v.count(x[i])
            contx = x.count(x[i])
            if cont < contx:
                i = tam_x 
                parou = 1
                print(f'O vetor x {x} não é subvetor do vetor v {v}.')
            i += 1
    
    if parou != 1:
        print(f'O vetor x {x} é subvetor do vetor v {v}.') 
         
    
    
    
    