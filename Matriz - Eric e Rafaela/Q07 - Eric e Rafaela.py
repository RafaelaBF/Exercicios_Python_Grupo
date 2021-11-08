'''Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre: (a) o maior elemento da matriz e sua respectiva posição (linha e coluna); (b) o menor elemento da matriz e sua respectiva posição.'''

matriz = []
for i in range(6):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Entre com A[{i}][{j}]:')))
    matriz.append(linha);

maior_linha = 0
maior_coluna = 0
maior = matriz[0][0]
for i in range(6):
    for j in range(3):        
        if maior < matriz[i][j]:
            maior = matriz[i][j]
            maior_linha = i
            maior_coluna = j

print(f"a) O número {maior} é o maior da matriz e sua posição é\nLinha do maior:{maior_linha}\nColuna do maior:{maior_coluna}")

menor_linha = 0
menor_coluna = 0
menor = matriz[0][0]
for i in range(6):
    for j in range(3):        
        if menor > matriz[i][j]:
            menor = matriz[i][j]
            menor_linha = i
            menor_coluna = j

print(f"\nb) O número {menor} é o menor da matriz e sua posição é \nLinha do maior:{menor_linha}\nColuna do menor:{menor_coluna}")