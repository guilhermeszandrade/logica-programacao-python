#Tabuada Fixa 

#Peça para o usuário digitar um número inteiro. Use um laço de repetição de 1 a 10 para calcular
# e exibir a tabuada desse número no formato X x 1 = Y. 

#Objetivo: Praticar operações aritméticas a cada iteração do laço.

numero = int(input("Digite um numero e direi tabuada!"))

print('******', 'TABUADA', '*******')

for multiplicador in range(1,11):
    print(f'{numero} x {multiplicador} = {numero * multiplicador}')