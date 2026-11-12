#Cálculo de Fatorial 

#Peça um número inteiro positivo ao usuário e calcule o seu fatorial usando o laço for
# (exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120). 

#Objetivo: Trabalhar com produto acumulado e controle decrescente ou crescente de limites.

numero = int(input("Digite um numero e eu direi seu fatorial: "))

fatorial = 1

for contadora in range(1, numero + 1):
    fatorial *= contadora
    
print(fatorial)
