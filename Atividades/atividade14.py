'''Triângulo de Asteriscos (Laços Aninhados) 

Peça ao usuário um número inteiro N para representar a altura de 
um triângulo. Use laços de repetição para gerar o seguinte padrão
no terminal (para N = 4): 


Plaintext 

* 
** 
*** 
**** 

Objetivo: Compreender laços dentro de laços (nested loops) e 
manipulação de saídas por linha. '''

altura = int(input("Digite a altura do triângulo: "))

for linha in range(altura + 1):
    for coluna in range(linha):
        print("*", end="")
    print()