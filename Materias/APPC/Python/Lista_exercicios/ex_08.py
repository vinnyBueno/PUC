"""Faça um programa em python que converte temperaturas expressas em graus Celsius
para graus Rankine. Seu programa deve solicitar a digitação do valor a ser convertido (C).
A relação entre graus Celsius e graus Rankine é R = (C+491.67)*1.8.
A menor temperatura possivel em graus Celsius é -273.15"""

print("\nPrograma que converte graus Celsius para graus Rankine")

try:
    celsius = float(input("Digite o graus Celsius: "))
except ValueError:
    print("\nSomente numeros devem ser digitados!")
else:
    if celsius < -273.15:
        print("\nO menor valor para graus celsius é de -273.15")
    else:
        rankine = (celsius * 9/5) + 491.67
        print(f"{celsius} graus Celsius é igual a {rankine:.2f} graus Rankine!")