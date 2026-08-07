"""Faça um programa em python que converte temperaturas expressas em graus Rankine
para graus Fahrenheit. Seuprograma deve solicitar a digitação do valor a ser convertido(R).
A menor temperatura possível em graus Rankine é 0 e em graus Fahrenheit é -459.67"""

print("Converssor de Rankine para Fahrenheit")

try:
    r = float(input("\nDigite a temperatura em Rankine: "))
except ValueError:
    print("\nSomente numeros devem ser digitados!")
else:
    if r < 0:
        print("\nA menor temperatura possivel é de 0")
    else:
        fahrenheit = r - 459.67
        if fahrenheit < -459.67:
            print(f"\nA menor temperatura para fahrenheit é de -459.67 e nesse caso deu {fahrenheit}")
        else:
            print(f"\n{r} graus rankine é igual a {fahrenheit} graus Fahrenheit")



print("\nFim do programa")