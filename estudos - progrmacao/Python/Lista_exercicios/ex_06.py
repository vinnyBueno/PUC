"""Faça um programa em python que converte temperaturas expressas em
graus Celsius para graus kelvin. Seu programa deve solicitar a digitação
do valor a ser convertido (C). A relação entre graus celsius e graus Kelvin é
K = C + 273.15. A menor temperatura possível en graus Celsius é -273.15"""

print("Programa que converte graus Celsius para graus kelvin\n")

try:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
except ValueError:
    print("\nSomente numeros devem ser digitados!")
else:
    if celsius < -273.15:
        print("\nA menor temperatura em Celsius possivel é de -273.15!")
    else:
        kelvin = celsius + 273.15
        print(f"{celsius} graus Celsius é igual a {kelvin} graus kelvin!")

