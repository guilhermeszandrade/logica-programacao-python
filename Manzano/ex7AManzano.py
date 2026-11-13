"""
Ler uma temperatura em graus Celsius e apresenta-lo convertida em graus Fahrenheit.
A conversao e F (9* C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura 
"""

grausCelsius = float(input("Digite a temperatura em graus Celsius: "))

grausFahrenheit = (9 * grausCelsius + 160) / 5

print("A temperatura em graus Fahernehit e: "+ str(grausFahrenheit), "Graus")