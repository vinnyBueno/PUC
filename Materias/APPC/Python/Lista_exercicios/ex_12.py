"""Faça um programa que converte temperatura expressas em graus Fahrenheit 
para graus Rankine. Seu programa de solicitar a digitação do valor a ser convertido (F).
A menor temperatura possível em graus Fahrenheit é -459.67 e em graus Rankine é 0."""


print("Converssor de Fahrenheit para rankine")

try:
    f = float(input("\nDigite a temperatura em Fahrenheit: "))
except ValueError:
    print("\nSomente numeros devem ser digitados")
else:
    if f < -459.67:
        print("\nA menor temperatura possivel é -459.67")
    else:
        rankine = f + 459.67
        if rankine <= 0:
            print(f"\nA menor temperatura para rankine é 0 e nesse caso deu {rankine}")
        else:
            print(f"{f} é igual a {rankine}")