'''Peça para o usuário digitar uma frase. Percorra cada caractere da string usando o for e conte quantas vogais 
(a, e, i, o, u — maiúsculas ou minúsculas) existem no texto informado. 
Objetivo: Praticar a iteração sobre sequências do tipo texto (str). '''

frase = str(input("Digite uma frase:")).casefold()

contador = 0

vogais = ['a', 'e', 'i', 'o', 'u']

for caractere in frase:
    if caractere in vogais:
        contador += 1

print(f"Existem {contador} vogais na frase.")