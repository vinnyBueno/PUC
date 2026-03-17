"""Faça um programa em python que converte temperaturas expressas em graus Kelvin para
graus Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (K).
A relação entre graus Celsius e graus Kelvin é C = K - 273.15. A menor temperatura em
Kelvin é 0."""

print("Programa que converte Kelvin para Celsius\n")

try:
    kelvin = float(input("Digite a temperatura em graus Kelvin: "))
except ValueError:
    print("\nSomente numeros devem ser digitados!")
else:
    if kelvin < 0:
        print("A menor temperatura para kelvin é 0!")
    else:
        celsius = kelvin - 273.15
        print(f"{kelvin} graus Kelvin é igual a {celsius} graus Celsius!")