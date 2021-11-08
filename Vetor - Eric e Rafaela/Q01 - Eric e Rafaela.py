'''
Questão 1: 
 
Alunos: Eric e Rafaela      
'''
lis = []
i = 0
while i == 0:
    vet = (input('Entre com os números:'))
    if vet == 'fim' or vet == 'Fim' or vet == 'FIM':
        print(lis)
        i+=1
    else:
        vet = int(vet)
        lis.append(vet)

lis2 = []
for i in lis:
    if i not in lis2:
        lis2.append(i)

c = len(lis2)
for i in range(c):
    cont = lis.count(lis2[i])
    if cont == 1:
        print(f"O número {lis2[i]} apareceu {cont} vez no vetor")
    else:
        print(f"O número {lis2[i]} apareceu {cont} vezes no vetor")
    

    
    
    
    
    
    
    
    
    
