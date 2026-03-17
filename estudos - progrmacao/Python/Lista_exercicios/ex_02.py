"""Faça um programa em python que solicite a digitação de três valores quaisquer, informando-os, em seguida, em ordem crescente"""

print("Programa que recebe três valores e mostra eles em ordem crescente")

try:
    n1 = int(input("\nDigite um valor: "))
except ValueError:
    print("\nSomente numeros inteiros e sem vírgula devem ser digitados")
else:
    try:
        n2 = int(input("\nDigite o segundo valor: "))
    except ValueError:
        print("\nSomente numeros inteiros e sem vírgula devem ser digitados")
    else:
        try:
            n3 = int(input("\nDigite o terceiro valor: "))
        except ValueError:
            print("\nSomente numeros inteiros e sem vírgula devem ser digitados")
        else:
            if n1 < n2 and n1 < n3:
                print(f"{n1}, {n2}, {n3}")
            elif n2 < n1 and n2 < n3:
                print(f"{n2}, {n1}, {n3}")
            else:
                print(f"{n3}, {n2}, {n1}")


print("\nPrograma finalizado")