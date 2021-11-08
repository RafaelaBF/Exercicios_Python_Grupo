# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:05:20 2021

@author: Rafaela e Eric
"""
'''
Questão 2
Faça um programa que leia uma frase e uma palavra e em seguida determine o número de vezes que a palavra aparece na frase. 
Exemplo: Frase:  Ana e Mariana gostam de banana. 
Palavra: ana 
Temos que a palavra ana ocorre 4 vezes na frase. 
Obs.: Seu programa não deve diferenciar letras minúsculas de maiúsculas. 

'''

frase = input("Entre com a frase: ")
frase = frase.lower()
frase = frase.strip()

palavra = input("Entre com a palavra: ")
palavra = palavra.lower()
palavra = palavra.strip()


inicio = 0
i = 0
fim = frase.find(palavra,inicio)

while fim != -1:
    i += 1
    inicio = fim + 1
    fim = frase.find(palavra,inicio)
    
print(f"Temos que a palavra {palavra} ocorre {i} vezes na frase")