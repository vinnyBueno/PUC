"""Faça um programa em python que converte temperaturas expressas em graus Kelvin
para graus Fahrenheit.Seu programa deve soliciar a digitação do valor a ser convertido (k).
A menor temperatura possível em graus Kelvin é 0 e graus Fahrenheit é -459.67"""


print("Conversor de Kelvin para graus Fahrenheit")

try:
    k = float(input("Digite a temperatura em graus Kelvin: "))
except ValueError:
    print("\nSomente numeros devem ser digitados")
else:
    if k < 0:
        print("\nA menor temperatura em graus fahrenheit é de 0!")
    else:
        fahrenheit = (k - 273.15) * 1.8 + 32
        if fahrenheit < -459.67:
            print(f"{fahrenheit:.2f} não existe")
        else:
            print(f"{k}ºk equivale a {fahrenheit:.2f} fahrenheit")


print("\nFim do programa")