"""Faça um programa em python que converte temperaturas expressas em graus celsius para graus fahrenheit.
Seu programa deve solicitar a digitação do valor a ser convertido (C).
A relação entre graus Celsius e graus Fahrenheit é F = C / 1.8 + 32. A menor temperatura possível em graus Celsius é -273.15"""


print("programa para converter graus celsius para graus fahrenheit\n")
try:
    tem = float(input("Digte a temperatura em graus celsius: "))
except ValueError:
    print("\nSomente numeros são permitidos")
else:
    if tem < -273.15:
        print("\nEssa temperatura não é possivel!")
    else:
        fahrenheit = tem * 1.8 + 32

        print(f"A temperatura {tem} graus celcius é igual a {fahrenheit} fahrenheit")