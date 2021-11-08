# -*- coding: utf-8 -*-
"""
Questão 8

Alunos: Eric e Rafaela
"""

M = []
turma = []

max_media_aluno = 0
aluno_maior_media = 0

turma_maior_media = 0

for t in range(2):
    tur = []
    for a in range(3):
        aluno = []     
        for n in range(2):
            aluno.append(int(input(f'Entre com aluno {a} da turma {t}: ')))
        
        aluno.append(float(sum(aluno)/2))
        
        if max_media_aluno < aluno[2]:
            max_media_aluno = aluno[2]
            aluno_maior_media = a
            
        tur.append(aluno)
    
    med_tur = 0    
    for i in range (3):
        med_tur += tur[i][0] + tur[i][1]
    
   
    turma.append( round((med_tur/6), 2))
    
    for j in range (3):
        if turma[t] < tur[j][2]:
            print(f'O aluno {j} da turma {t} teve média maior que a média de sua turma com {tur[j][2]}')
        
    
    M.append(tur)
    
    
if turma[0] < turma[1]:
    turma_maior_media = 1
    
    
print(f'A média da turmas turmas foram: {turma}')
print(f'A turma que teve a maior média foi a turma: {turma_maior_media} com {turma[turma_maior_media]}')
