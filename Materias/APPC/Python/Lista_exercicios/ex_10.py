"""Levando em conta as relações entre unidades de temperaturas expressas
em graus Rankine para graus kelvin. Seu programa deve solicitar a digitação
do valor a ser convertido (F) a menor temperatura possivel em graus Fahrenheit é -459.67
e en graus Kelvin é 0"""

print("Conversor de graus Fahrenheit para graus Kelvin")

try:
    f = float(input("\nDigite uma temperatura em Fahrenheit: "))
except ValueError:
    print("\nDigite somente numeros!")
else:
    if f < -459.67:
        print("\nA menor temperatura possivel em graus Fahrenheit é -459.67")
    else:
        kelvin = (f - 32) * 5/9 + 273.15
        if kelvin < 0:
            print("A menor temperatura possivel em graus Kelvin é 0")
            print(f"{f}ºf equivalem a {kelvin:.2f}")


print("\nFim do programa")