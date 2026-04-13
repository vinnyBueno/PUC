def quantidade_bolinhas():
    rodaPrograma = True
    while rodaPrograma:
        try:
            numero = int(input("\nDigite um número maior ou igual a 2: "))
        except ValueError:
            print("Erro: você deve digitar um número inteiro!")
        else:
            if numero < 2:
                print("Erro: o número deve ser maior ou igual a 2")
            else:
                rodaPrograma = False
    return numero


def mostra_bolinhas(numero):
    i = 1
    while i <= numero:
        espacos = numero - i
        letras = 2 * i - 1
        print(" " * espacos, end="")
        print("O" * letras)
        i += 1
    

print("Programa que gera uma pirâmide com a letra O")

rodaPrograma = False
while not rodaPrograma:
    qtdBolas = quantidade_bolinhas()

    resultado = mostra_bolinhas()
    print(resultado)