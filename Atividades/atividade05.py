#Nível 2: Acumuladores e Operações 

#Soma Manual de Elementos 

#Dada a lista numeros = [12, 45, 7, 23, 56, 89, 3], calcule a soma de todos os números 
# utilizando um laço for e uma variável acumuladora (sem usar a função embutida sum()). 
#Objetivo: Compreender o padrão de acumulador (total += item). 

numeros = [12, 45, 7, 23, 56, 89, 3]
total = 0

for numero in numeros: 
    total += numero
    print(f'A soma {numero}, é {total}')