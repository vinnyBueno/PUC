"""Faça um programa em python que converte temperaturas expressas em graus Kelvin para para Rankine.
Seu programa deve solicitar a digitação do valor a ser convertido (K).
A menor temperatura possível em graus Kelvin é 0 e em graus Rankine também é 0."""

print("\nConverssor de Kelvin para Rankine")

try:
    k = float(input("\nDigite a temperatura em kelvin: "))
except ValueError:
    print("\nSomente numeros devem ser digitados!")
else:
    if k <0:
        print("\nA menor temperatura aceita para kelvin é 0.")
    else:
        rankine = k * 1.8
        if rankine < 0:
            print(f"\nA menor temperatura para rankine é 0 nesse caso deu {rankine}")