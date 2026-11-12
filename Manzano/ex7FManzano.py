"""Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, e efetuar a troca dos valores de
forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da
variável A. Apresentar os valores trocados"""

print("****PROGRAMA TROCA DE VALORES****")

valor01 = int(input("DIGITE O PRIMEIRO VALOR: "))
valor02 = int(input("DIGITE O SEGUNDO VALOR: "))

valor01, valor02 = valor02, valor01

print("O VALORES TROCADOS ENTRE AS VARIAVEIS É: ", valor01, " : ", valor02)