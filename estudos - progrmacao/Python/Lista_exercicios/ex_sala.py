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
                        print(f"\n{hora}:{minutos}:{segundos}")
                        try:
                            qtdSegundos = int(input("\nAgora digite quantos segundo você quer adiantar: "))
                        except ValueError:
                            print("\nSegundos deve ser numerico")
                        else:

                            total = hora * 3600 + minutos * 60 + segundos + qtdSegundos


                            total = total % 86400

                            hora = total // 3600
                            total = total % 3600

                            minutos = total // 60
                            segundos = total % 60

                            print(f"\nNovo horario: {hora:02d}:{minutos:02d}:{segundos:02d}")