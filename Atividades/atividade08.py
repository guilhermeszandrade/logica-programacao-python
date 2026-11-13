'''Identificar Maior e Menor Valor 
Dada a lista valores = [34, 12, 89, 5, 72, 43], encontre o maior e o menor valor contido nela usando apenas 
iteração e estruturas condicionais if, sem recorrer às funções max() e min(). 
Objetivo: Aprender a manter e atualizar o estado de variáveis sentinelas durante a varredura de dados. '''

valores = [34, 12, 89, 5, 72, 43]

maior_valor = 0

for valor in valores:
    if maior_valor < valor:
        maior_valor = valor
        menor_valor = maior_valor
        
    if menor_valor > valor:
        menor_valor = valor
        
print(f"menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")