"""Solução feita pelo professor"""

print("PROGRAMA PARA ADIANTAR HORARIOS\n")

try:
    hora=int(input("Hora? "))
except ValueError:
    print("Hora deve ser numerica!")
else:
    if hora<0 or hora>23:
        print("So ha horas entre 0 e 23!")
    else:
        try:
            minuto=int(input("Minuto? "))
        except ValueError:
            print("Minuto deve ser numerico!")
        else:
            if minuto<0 or minuto>59:
                print("So ha minutos entre 0 e 59!")
            else:
                try:
                    segundo=int(input("Segundo? "))
                except ValueError:
                    print("Segundo deve ser numerico!")
                else:
                    if segundo<0 or segundo>59:
                        print("So ha segundos entre 0 e 59!")
                    else:
                        try:
                            qtdSegs=int(input("Quer adiantar quantos segundos? "))
                        except ValueError:
                            print("Quantidades devem ser numericas!")
                        else:
                            if qtdSegs<=0:
                                print("So pode adiantar quantidades positivas de segundos!")
                            else:
                                tempo=segundo-qtdSegs # em segundos; valor pode ser grande
                                segundo=tempo%60
                                tempo=tempo//60 + minuto # em minutos; valor pode ser grande
                                minuto=tempo%60
                                tempo=tempo//60 + hora # em horas; valor pode ser grande
                                hora=tempo%24
                                #tempo=tempo//24 # em dias; valor pode ser grande e desprezo
                                if hora<10: hora="0"+str(hora)
                                if minuto<10: minuto="0"+str(minuto)
                                if segundo<10: segundo="0"+str(segundo)
                                print("Adiantado conforme solicitado, o horario fica ",hora,":",minuto,":",segundo,sep="")

print("\nPROGRAMA ENCERRADO")