"""Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um
automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto
(TEMPO) e a velocidade média (VELOCIDADE) durante a viagem. Desta forma, será possível obter a
distância percorrida com a fórmula DISTANCIA  TEMPO * VELOCIDADE. Possuindo o valor da
distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula
LITROS_USADOS  DISTANCIA / 12. Ao final, o programa deve apresentar os valores da velocidade
média (VELOCIDADE), tempo gasto na viagem (TEMPO), a distancia percorrida (DISTANCIA) e a
quantidade de litros (LITROS_USADOS) utilizada na viagem."""

print("****PROGRAMA LITRO COMBUSTIVEL****")

tempo = float(input("DIGITE O TEMPO GASTO EM VIAGEM: "))
velocidadeMedia = float(input("DIGITE A VELOCIDADE MEDIA DA VIAGEM: "))

distanciaPercorrida = tempo * velocidadeMedia
litrosUsados = distanciaPercorrida / 12

print("O TEMPO GASTO DURANTE A VIAGEM FOI DE: ", tempo, "H")
print("A VELOCIDADE MEDIA DA VIAGEM FOI DE: ", f'{velocidadeMedia:.2f}'+ "km/h")
print("A DISTANCIA PERCORRIDA DURANTE A VIAGEM FOI DE: ", f'{distanciaPercorrida:.2f}',"metros ")
print("A QUANTIDADE DE LITROS DE COMBUSTIVEL UTILIZADOS DURANTE A VIAGEM FOI DE: ",f'{litrosUsados:.2f}'"litros")