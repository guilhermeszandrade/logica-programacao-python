'''
Dada uma lista de dados cadastrais brutos como: 
registros = [" ana silva ", "JOAO ", " ", "MARIA souza", "pedro santos "] 
Crie uma nova lista apenas com os nomes válidos (removendo os vazios ou com apenas espaços), 
com os espaços extras eliminados nas pontas e todos formatados em letras maiúsculas e minúsculas corretas
(Title Case). Exiba a lista limpa e a quantidade de registros descartados. 
Objetivo: Aplicar o laço for em um fluxo completo de tratamento, validação e transformação de dados.
'''

registros = [" ana silva ", "JOAO ", " ", "MARIA souza", "pedro santos "] 

nomes_validos = []

for nome in registros:
    nome = nome.strip().title()
    
    if len(nome) != 0:
        nomes_validos.append(nome)

print(nomes_validos)