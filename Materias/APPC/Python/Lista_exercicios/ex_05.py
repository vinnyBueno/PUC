"""Faça um programa em python que converte temperaturas expressas em graus Fahrenheit para graus Celsius.
Seu programa deve solicitar a digitação do valor a ser convertido (F). A relação entre
graus Celsius e graus Fahrenheit é C = 5/9 * (F-32). A menor temperatura possivle em graus Fahrenheit é -459.67"""


print("Programa Fahrenheit para Celsius\n")

try:
    fah = float(input("Digite a temperatura em graus Celsius: "))
except ValueError:
    print("\n Digite somente numeros e não letras!")
else:
    if fah < -459.67:
        print("\nTemperatura não permitida!")
    else:
        celsius =  5/9  * (fah - 32)
        print(f"A temperatura {fah} fahrenheit é igual a {celsius:.2f} graus Celsius!.")

print("\nFim do programa")