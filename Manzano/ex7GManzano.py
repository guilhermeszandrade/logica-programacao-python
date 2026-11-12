"""Ler quatro números inteiros e apresentar o resultado da adição e multiplicação, baseando-se na
utilização do conceito da propriedade distributiva. Ou seja, se forem lidas as variáveis A, B, C, e D,
devem ser somadas e multiplicadas A com B, A com C e A com D. Depois B com C, B com D e por fim
C com D. Perceba que será necessário efetuar seis operações de adição e seis operações de
multiplicação e apresentar doze resultados de saída."""

print("****PROGRAMA QUATRO NUMEROS INTEIROS****")

valor01 = int(input("DIGITE O PRIMEIRO VALOR: "))
valor02 = int(input("DIGITE O SEGUNDO VALOR: "))
valor03 = int(input("DIGITE O TERCEIRO VALOR: "))
valor04 = int(input("DIGITE O QUARTO VALOR: "))

soma01 = valor01 + valor02
soma02 = valor01 + valor03
soma03 = valor01 + valor04
soma04 = valor02 + valor03
soma05 = valor02 + valor04
soma06 = valor03 + valor04

multiplicacao01 = valor01 * valor02
multiplicacao02 = valor01 * valor03
multiplicacao03 = valor01 * valor04
multiplicacao04 = valor02 * valor03
multiplicacao05 = valor02 * valor04
multiplicacao06 = valor03 * valor04

print("O RESULTADO DAS SOMAS ENTRE OS VALORES É: ", "A + B = ", soma01," : " "A + C = ", soma02,
    " : ", "A + D = ", soma03, " : ", "B + C = ",soma04, " : ", "B + D = ", soma05, " : ", "C + D = ", soma06 )

print("O RESULTADO DA MULTIPLICACAO ENTRE OS VALORES É: ", "A + B = ", multiplicacao01," : " "A + C = ", multiplicacao02,
    " : ", "A + D = ", multiplicacao03, " : ", "B + C = ",multiplicacao04, " : ", "B + D = ", multiplicacao05, " : ", "C + D = ", multiplicacao06 )

