'''
Implemente duas novas opções, uma para contar quantas vezes aparece na lista o número dado
e outra para ordenar os numeros da lista pelo método da bolha (bubble sort)
'''

def opcao_escolhida ():
    print("1) Esvaziar a lista")
    print("2) Incluir número na lista")
    print("3) Excluir número dando o número")
    print("4) Excluir número dando sua posição")
    print("5) Mostrar a lista")
    print("6) Somar tudo da lista")
    print("7) Achar o menor")
    print("8) Achar o maior")
    print("9) Sair do programa")
    
    chave_para_escolher_opcao_ate_acertar_ligada=True
    while chave_para_escolher_opcao_ate_acertar_ligada:
        try:
            opcao=int(input("Opcao? "))
        except ValueError:
            print("Opção inválida; tente novamente!")
        else:
            if opcao<1 or opcao>9:
                print("Opção inválida; tente novamente!")
            else:
                chave_para_escolher_opcao_ate_acertar_ligada=False

    return opcao

def esvazia_lista (lista):
    lista.clear()
    print("Esvaziamento realizado com sucesso!")

def numero_digitado(proposito, aceitavel=None):
    chave_para_digitar_um_numero_ate_acertar_ligada=True
    while chave_para_digitar_um_numero_ate_acertar_ligada:
        try:
            numero=float(input("Qual número deseja "+proposito+"? ", sep=""))
        except ValueError:
            print("Foi pedido um número para ",proposito,"; tente novamente!", sep="")
        else:
            if aceitavel != None and numero not in aceitavel:
                print("Numero inaceitavel para ",proposito,"; tente novamente!", sep="")
            else:
                chave_para_digitar_um_numero_ate_acertar_ligada=False
    return numero

def incluir_numero (lista):
    numero=numero_digitado("incluir", None)
    lista.append(numero)
    print("Número incluido com sucesso!")

def excluir_numero_dado_o_numero(lista):
    numero=numero_digitado("excluir", lista)
    if numero in lista:
        lista.remove(numero)
        print("Número excluido com sucesso!")
    else:
        print("O numero não existe na lista!")

def excluir_numero_dada_a_posição(lista):
    chave_para_digitar_um_numero_ate_acertar_ligada=True
    while chave_para_digitar_um_numero_ate_acertar_ligada:
        try:
            posicao=int(input("Qual posição deseja excluir?"))
        except ValueError:
            print("Foi pedida uma posição; eles devem ser números inteiros. tente novamente!")
        else:
            if posicao <0 or posicao>=len(lista):
                print("Posição inaceitavel; tente novamente!")
            else:
                chave_para_digitar_um_numero_ate_acertar_ligada=False
    del lista[posicao]
    print("Número na posição desejada excluido com sucesso!")


def soma (lista):
    resultado=0
    posicao=0
    while posicao<len(lista):
        resultado+=lista[posicao]
        posicao+=1
    return resultado

def mostrar_soma (lista):
    print("A soma vale",soma(lista))


def o_menor (lista):
    menor=lista[0]
    posicao=1
    while posicao<len(lista):
        if lista[posicao]<menor:
            menor=lista[posicao]
        posicao+=1
    return menor

def o_maior (lista):
    maior=lista[0]
    posicao=1
    while posicao<len(lista):
        if lista[posicao]>maior:
            maiorr=lista[posicao]
        posicao+=1
    return maior




def executar_opcoes (lista):
    chave_para_realizar_operacoes_ate_cansar_ligada=True
    while chave_para_realizar_operacoes_ate_cansar_ligada:
        opcao=opcao_escolhida()

        if opcao==1:
            esvazia_lista(lista)
        elif opcao==2:
            incluir_numero(lista)
        elif opcao==3:
            excluir_numero_dado_o_numero(lista)
        elif opcao==4:
            mostrar_soma (lista)
        elif opcao==5:
            o_menor (lista)
        elif opcao==6:
            o_maior (lista)
        elif opcao==7:
            ...
        elif opcao==8:
            ...
        else: # só sobrou a opcao ser 9
            chave_para_realizar_operacoes_ate_cansar_ligada=False

# DAQUI PARA CIMA DEFINIMOS SUBPROGRAMAS
# DAQUI PARA BAIXO FIZEMOS O PROGRAMA, CHAMANDO NELE OS SUBPROGRAMAS ACIMA

print("PROGRAMA PARA REALIZAR OPERAÇÕES COM LISTAS\n")

lista=[] # lista começa vazia
executar_opcoes (lista)

print("PROGRAMA ENCERRADO!")