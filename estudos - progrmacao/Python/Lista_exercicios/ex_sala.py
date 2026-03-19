print("Programa para valider se horas são válidas")


try:
    hora = int(input("Digite hora: "))
except ValueError:
    print("\nHora deve ser numerica!")
else:
    if hora < 0 or hora > 23:
        print("\nHorario invalido")
    else:
        try:
            minutos = int(input("\nDigite os minutos: "))
        except ValueError:
            print("\nMinuto deve ser numerico!")
        else:
            if minutos < 0 or minutos > 59:
                print("\nMinuto invalido!")
            else:
                try:
                    segundos = int(input("\nDigite segundos: "))
                except ValueError:
                    print("\nSegundos deve ser numerico!")
                else:
                    if segundos < 0 or segundos > 60:
                        print("\nSegundos invalidos!")
                    else:
                        try:
                            qtdSegundos = int(input("\nAgora digite quantos segundo você quer adiantar: "))
                        except ValueError:
                            print("\nSegundos deve ser numerico")
                        else:
                            if qtdSegundos <= 0:
                                print("quantidade deve ser positivo!")
                            else:
                                segundos = segundos + qtdSegundos
                                if segundos > 60:
                                    qtdSegundos = qtdSegundos - segundos
                                    segundos = 0
                                else:
                                    minutos = minutos = qtdSegundos

                                    
                                
