'''
Crie uma lista de cidades. Peça ao usuário para digitar o nome de uma cidade. 
Percorra a lista para verificar se a cidade está presente. Se encontrar, informe o 
índice em que ela está e interrompa a busca usando break. Caso o laço termine sem encontrar, 
avise que a cidade não está cadastrada. 
Objetivo: Aplicar controle de fluxo com break e verificação de condições de parada.
'''

cidades = ['franco da rocha', 'osasco', 'brasilandia', 'são paulo', 'são mateus', 'perus', 'guarulhos', 'cajamar']

cidade_busca = str(input("Qual é a melhor cidade de São Paulo: "))



for indice, cidade in enumerate(cidades):
    if cidade == cidade_busca:
        print(f"A cidade: {cidade}, é o indice: {indice}")
        break
else:
    print("Cidade não encontrada!")