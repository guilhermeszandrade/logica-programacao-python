"""Calcular e apresentar o valor do volume de uma lata de óleo, 
utilizando a fórmula:Volume *Raio * Altura"""

print("****PROGRAMA VOLUME****")

raio = float(input("DIGITE O VALOR DO RAIO DA LATA DE OLEO: "))

altura = float(input("DIGITE O VALOR DO ALTURA DA LATA DE OLEO: "))

pi = 3.14

volume = pi * (raio**2) * altura

print("O VOLUME DA LATA DE OLEO É: ", f'{volume:.2f}')