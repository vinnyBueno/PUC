print("\t\tprograma para solucionar equações de segundo grau")
try:
   A = float(input("\nDigite o valor de A: "))
except ValueError:
    print("\nEspera-se que seja digitado um numero!")
else:
    if A==0:
        print('\nEquaçoes de segundo grau não podem ter o coeficiente "A" igual a 0')
    else:
        try:
            B = float(input("\nDigite o valor de B: "))
        except ValueError:
            print("\nEspera-se que seja digitado um numero!")
        else:
            try:
                C = float(input("\nDigite o valor de C: "))
            except ValueError:
                print("\nEspera-se que seja digitado um numero!")
            else:
                delt = B**2 - 4*A*C
                

                if delt < 0:
                    print("A equação não possui raiz (delta negativo)")
                elif delt == 0:
                    x = -B / (2*A)
                    print (f"uma raiz real: {x}")
                else:
                    x1 = (-B + (delt**0.5)) / (2*A)
                    x2 = (-B - (delt** 0.5)) / (2*A)
                    print(f"Duas raízes reais: x1 = {x1}, x2 = {x2}")
                
print("\nPrograma encerrado!!!")