matriz = []
aux = 0
media = 0
melhor_tempo = 0
melhor_corredor = ""
media_melhor_volta = 0
volta_mais_rapida = 0
matriz_sorted = []
primeiro_lugar = 0
for i in range(6):
    linha = []
    linha_n = []
    corredor = input('Entre com o nome do corredor:  ')
    linha.append(corredor)
    for j in range(10):
        tempo = float(input(f"Entre com o tempo {j} da volta do corredor {corredor}:  "))
        if(aux == 0):
            melhor_tempo = tempo
            melhor_corredor = corredor
            melhor_volta = j
            aux += 1
        linha.append(tempo)
        linha_n.append(tempo)
        if(tempo < melhor_tempo):
            melhor_tempo = tempo
            melhor_corredor = corredor
            melhor_volta = j
    matriz.append(linha)
    linha_n = [sum(linha_n)]
    linha_n.append(corredor)
    matriz_sorted.append(linha_n)
for j in range(1, 10 + 1):
    media = 0
    for i in range(6):
        media += matriz[i][j]
    media /= 6
    if(aux == 1):
        media_melhor_volta = media
        volta_mais_rapida = j
        aux += 1
    if(media < media_melhor_volta):
       media_melhor_volta = media
       volta_mais_rapida = j
matriz_sorted = sorted(matriz_sorted)
print(f'\nA melhor volta foi do {melhor_corredor[0].upper() + melhor_corredor[1:len(melhor_corredor)]}, na volta {melhor_volta}')
print('\nPlacar final:')
print('\nColocação / Tempo médio / Tempo total')
for i in range(6):
    print(f'{i+1}º - {matriz_sorted[i][1]} / {matriz_sorted[i][0]/10:.1f}s / {matriz_sorted[i][0]}s')
print(f'\nA volta com a média mais rápida foi a {melhor_volta}.')