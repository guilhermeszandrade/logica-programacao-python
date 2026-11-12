#Média de Notas 

#Crie uma lista com 4 notas decimais de um aluno. Percorra a lista acumulando a soma e,
#ao final do laço, calcule e exiba a média aritmética simples. 

#Objetivo: Combinar o padrão acumulador com processamento após o término do loop. 

materias = int(input("Quantas matérias o aluno tem? "))
notas = 0

for contadora in range(materias):
    notas += float(input(f"Digite a nota da matéria {contadora + 1}: "))

media = notas / materias

print(f"A média do aluno é de {media:.2f}")

if media > 6:
    print("Parabens! O aluno passou de ano!")
else:
    print("O Aluno reprovou de ano!")