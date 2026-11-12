"""Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a fórmula
PRESTACAO <- VALOR + (VALOR * TAXA/100) * TEMPO).""" 

print("****PROGRAMA PRESTACAO****")

valorPrestacao = float(input("DIGITE O VALOR DA PRESTACAO DO CLIENTE: "))
taxaPrestacao = float(input("DIGITE A TAXA DA PRESTACAO DO CLIENTE: "))
tempoPrestacao = float(input("DIGITE OS DIAS DE ATRASO DA PRESTACAO: "))

prestacao = valorPrestacao + (valorPrestacao * taxaPrestacao/100) * tempoPrestacao

print("O VALOR DA PRESTACAO A PAGAR, APOS O ATRASO E DE: ", f'{prestacao:.2f}'"R$")