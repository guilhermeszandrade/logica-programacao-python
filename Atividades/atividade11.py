'''
Dada a lista competidores = ["Mariana", "Lucas", "Beatriz", "Carlos"], use a função enumerate() para 
imprimir a posição de cada um formatada como: 
1º lugar: Mariana 
2º lugar: Lucas 
Objetivo: Aprender a obter simultaneamente o índice e o elemento durante a iteração.
'''
competidores = ["Mariana", "Lucas", "Beatriz", "Carlos", "Daniel"]

for contador, nome  in enumerate(competidores):
    print(f"{contador + 1}º lugar - {nome}")