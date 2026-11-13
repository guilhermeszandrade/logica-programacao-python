'''
Dada uma lista de 10 números inteiros quaisquer, crie duas novas listas vazias: pares e impares.
Percorra a lista original e adicione cada número à sua respectiva lista dependendo de sua paridade (% 2). 
Objetivo: Integrar tomadas de decisão (if/else) e métodos de lista (.append()) dentro do laço. 
'''

numero_inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []

for valor in numero_inteiros:
    if valor % 2:
        impares.append(valor)
    else:
        pares.append(valor)

print(f"valores pares: {pares}")
print(f"valores impares: {impares}")