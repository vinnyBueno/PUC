# 1 Faça um programa em python que solicite a digitação de dois valores quaisquer, informando - os, em seguida em ordem crescente.

print("Programa que mostra em ordem crescente dois valores que são digitados")
try:
    n1 = int(input("\n\nDigite o primeiro valor: "))
except ValueError:
    print("\nSomente numeros inteiros sem virgula devem ser digitados!")
else:
    try:
        n2 = int(input("\nDigite o segundo valor: "))
    except ValueError:
        print("\nSomente numeros inteiros sem virgula devem ser digitados!")
    else:
        if n1 < n2:
            print(f"a ordem fica {n1}, {n2}")
        else:
            print(f"a ordem fica {n2}, {n1}")