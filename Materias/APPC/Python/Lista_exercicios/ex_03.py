"""Faça um programa em python que solicite a digitação de quatro valores quaisquer, informando-os, em seguinda, em ordem crescente"""

print("Programa que recebe quatro valores e mostra eles em ordem crescente")

try:
    n1 = int(input("\nDigite o primeiro valor: "))
except ValueError:
    print("\nO primeiro valor precisa ser um numero inteiro sem vírgula")
else:
    try:
        n2 = int(input("\nDigite o segundo valor: "))
    except ValueError:
        print("\nO segundo valor precisa ser um numero inteiro sem vírgula")
    else:
        try:
            n3 = int(input("\nDigite o terceiro valor: "))
        except ValueError:
            print("\nO terceiro valor precisa ser um numero inteiro sem vírgula")
        else:
            try:
                n4 = int(input("\nDigite o quarto valor: "))
            except ValueError:
                print("\nO quarto valor precisa ser um numero inteiro sem vírgula")
            else:

                # pegando o menor
                if n1 <= n2 and n1 <= n3 and n1 <= n4:
                    menor = n1
                elif n2 <= n1 and n2 <= n3 and n2 <= n4:
                    menor = n2
                elif n3 <= n1 and n3 <= n2 and n3 <= n4:
                    menor = n3
                else:
                    menor = n4

                # pegando o maior
                if n1 >= n2 and n1 >= n3 and n1 >= n4:
                    maior = n1
                elif n2 >= n1 and n2 >= n3 and n2 >= n4:
                    maior = n2
                elif n3 >= n1 and n3 >= n2 and n3>= n4:
                    maior = n3
                else:
                    maior = n4

                # pegando os dois do meio
                if n1 != menor and n1 != maior:
                    meio1 = n1
                elif n2 != menor and n2 != maior:
                    meio1 = n2
                elif n3 != menor and n3 != maior:
                    meio1 = n3
                else:
                    meio1 = n4

                #pegando o segundo meio
                if n1 != menor and n1 != maior and n1 != meio1:
                    meio2 = n1
                elif n2 != menor and n2 != maior and n2 != meio1:
                    meio2 = n2
                elif n3 != menor and n3 != maior and n3 != meio1:
                    meio2 = n3
                else:
                    meio2 = n4

                if meio1 <= meio2:
                    print(f"{menor}, {meio1}, {meio2}, {maior}")
                else:
                    print(f"{menor}, {meio2}, {meio1}, {maior}")

print("Fim do programa!!")