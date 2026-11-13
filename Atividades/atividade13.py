'''
Crie um dicionário onde a chave é o nome de um produto e o valor é o preço unitário 
(ex: {"Teclado": 150.0, "Mouse": 80.0, "Monitor": 900.0}). Use o laço for com o método .items()
para percorrer e imprimir cada produto, seu preço e, ao final, o total somado de todos os itens. 
Objetivo: Entender o desempacotamento de pares chave-valor durante a iteração de dicionários. 
'''

produtos = {"Teclado": 150.56, "Mouse": 80.2, "Monitor": 900.7}

preco_total = 0

for produto, preco in produtos.items():
    print(f"Produto: {produto}, Preço: R${preco}")
    preco_total += preco

print(f"O valor total dos produtos é: R${preco_total:.2f}")