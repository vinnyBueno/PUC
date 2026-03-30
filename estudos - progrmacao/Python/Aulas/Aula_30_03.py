'''
PROGRAMA PARA CONVERTER TEMPERATURAS

 1) DE CELSIUS    PARA FAHRENHEIT
 2) DE CELSIUS    PARA KELVIN
 3) DE CELSIUS    PARA RANKINE
 4) DE FAHRENHEIT PARA CELSIUS
 5) DE FAHRENHEIT PARA KELVIN
 6) DE FAHRENHEIT PARA RANKINE
 7) DE KELVIN     PARA CELSIUS
 8) DE KELVIN     PARA FAHRENHEIT
 9) DE KELVIN     PARA RANKINE
10) DE RANKINE    PARA CELSIUS
11) DE RANKINE    PARA FAHRENHEIT
12) DE RANKINE    PARA KELVIN

Sua opcao? 13
Opcao invalida!

PROGRAMA TERMINADO COM SUCESSO!
-----------------------------------------------------------------------------
PROGRAMA PARA CONVERTER TEMPERATURAS

 1) DE CELSIUS    PARA FAHRENHEIT
 2) DE CELSIUS    PARA KELVIN
 3) DE CELSIUS    PARA RANKINE
 4) DE FAHRENHEIT PARA CELSIUS
 5) DE FAHRENHEIT PARA KELVIN
 6) DE FAHRENHEIT PARA RANKINE
 7) DE KELVIN     PARA CELSIUS
 8) DE KELVIN     PARA FAHRENHEIT
 9) DE KELVIN     PARA RANKINE
10) DE RANKINE    PARA CELSIUS
11) DE RANKINE    PARA FAHRENHEIT
12) DE RANKINE    PARA KELVIN

Sua opcao? 4

Temperatura original? 69
Temperatura convertida: 20

PROGRAMA TERMINADO COM SUCESSO!
-----------------------------------------------------------------------------
'''
roda_programa = True
while roda_programa == True:
    
    
    print("PROGRAMA PARA CONVERTER TEMPERATURAS")

    print(" 1) DE CELSIUS    PARA FAHRENHEIT")
    print(" 2) DE CELSIUS    PARA KELVIN")
    print(" 3) DE CELSIUS    PARA RANKINE")
    print(" 4) DE FAHRENHEIT PARA CELSIUS")
    print(" 5) DE FAHRENHEIT PARA KELVIN")
    print(" 6) DE FAHRENHEIT PARA RANKINE")
    print(" 7) DE KELVIN     PARA CELSIUS")
    print(" 8) DE KELVIN     PARA FAHRENHEIT")
    print(" 9) DE KELVIN     PARA RANKINE")
    print("10) DE RANKINE    PARA CELSIUS")
    print("11) DE RANKINE    PARA FAHRENHEIT")
    print("12) DE RANKINE    PARA KELVIN")
    print("13) Sair do programa")

    try:
        opcao=int(input("Sua opcao? "))
    except ValueError:
        print("Opcao invalida!")
    else:
        if opcao<1 or opcao>13:
            print("Opcao invalida!")
        else:
            # digito_correto = False
            if opcao==13:
                roda_programa = False
            else:
                original=float(input("Temperatura a converter? "))
                if opcao==1: # quero converter de Celsius para Fahrenheit
                    if original<273.15:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original*1.8+32
                elif opcao==2: # quero converter de Celsius para Kelvin
                    if original<273.15:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original+273.15
                elif opcao==3: # quero converter de Celsius para Rankine
                    if original<273.15:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=(original+491.67)*1.8
                elif opcao==4: # quero converter de Fahrenheit para Celsius
                    if original<-459.67:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=(original-32)/1.8
                elif opcao==5: # quero converter de Fahrenheit para Kelvin
                    if original<-459.67:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=(original+459.67)*5/9
                elif opcao==6: # quero converter de Fahrenheit para Rankine
                    if original<-459.67:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original+459.67
                elif opcao==7: # quero converter de Kelvin para Celsius
                    if original<0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original-273.15
                elif opcao==8: # quero converter de Kelvin para Fahrenheit
                    if original<0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida= (original -273.15)*1.8+32
                elif opcao==9: # quero converter de Kelvin para Rankine
                    if original<0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original*1.8
                elif opcao==10: # quero converter de Rankine para Celsius
                    if original<0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original/1.8-491.67
                elif opcao==11: # quero converter de Rankine para Fahrenheit
                    if original<0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original-459.67
                elif opcao==12: # quero converter de Rankine para Kelvin
                    if original<0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO!")
                    else:
                        convertida=original/1.8

                if 'convertida' in vars(): print("Temperatura convertida:",convertida)

print("programa encerrado")