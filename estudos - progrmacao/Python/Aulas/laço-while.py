print("Programa para calcular areas de quadrado\n")
chave_de_calculo_de_area_ligada = True
while chave_de_calculo_de_area_ligada:
    chave_de_ligacao_ligada = True
    while chave_de_ligacao_ligada:
        try:
            lado = float(input("Media em cm do lado? "))
        except ValueError:
            print("\nLados de quadrado devem ter medidas numericas; tente novamente")
        else:
            if lado<=0:
                print("Lado de quadrado deve ser positivo; tente novamente")
            else:
                chave_de_ligacao_ligada = False

    area = lado **2
    print(f"A area do quadrado indicado vale {area} centimetros quadrados")

    chave_de_digitacao_de_resposta_ligada = True
    while chave_de_digitacao_de_resposta_ligada:
        resposta = input("Deseja calcular a area de mais algum quadrado (S/N)? ").upper()
        
        if resposta!= "N" and resposta != "S": 
            print("\nDeve se responder com S ou N")
        else:
            chave_de_digitacao_de_resposta_ligada=False

    if resposta == "N": chave_de_calculo_de_area_ligada = False
print("Fim do progrma")