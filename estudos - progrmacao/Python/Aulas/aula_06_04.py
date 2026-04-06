"""
anotar no caderno!!

Subprogramas

Progrmas são frequentemente longos e complexos apresentando muitas vezes trecho de codigos replicados (ou quase) e, para organizar tudo isso usamos subprogramas.
Subprogramas são um trecho de logica de programação, não um programa completo. Eles têm nome e eventualmente podem ter parametros(dados fornecidos ao chamarmos o programa) e retorno ( dados fornecidos pelo subprograma para serem usados por quem o chamou).
retorno nem sempre existe, mas, quando existe faz do subprograma uma função e, quando inexiste faz do subprograma um procedimento. 
São definidos usando a palabra def, na frente da qual escreveremos o nome do subprograma e mais na frente entre parenteses, escreveremos os nomes dos eventoais parametros. Os parenteses sempre existiram, mesmo que não haja nada entre eles.
Quando ouver um retorno ele sera expresso pelo comanto return diante do qual escreveremos um valor ou uma expressão que resulte um valor que é o que será retornado. 
Procedimentos não costumam ter o comando return mas quando tem, tem apenas a palavra return, sem nada escrito diante dela e, neste caso, servem apenas para encerrar o subprograma e não para transmitir um valor para quem chamou. 
""" 

def soma_dos_divisores (X):
    # soma os divisores de sem incluir X
    soma_dos_divisores_de_X=1
    possivel_divisor_de_X=2
    metade_de_X=X//2
    
    while possivel_divisor_de_X<=metade_de_X:
        if X%possivel_divisor_de_X==0:
            soma_dos_divisores_de_X+=possivel_divisor_de_X
        possivel_divisor_de_X+=1
        
    return soma_dos_divisores_de_X
'''    
def sao_amigos (A,B):
    soma_dos_divisores_de_A=soma_dos_divisores(A)
    soma_dos_divisores_de_B=soma_dos_divisores(B)
    
    if A==soma_dos_divisores_de_B and B==soma_dos_divisores_de_A
        return True
    else:
        return False
'''    
def sao_amigos (A,B):
    if soma_dos_divisores(A)==B and soma_dos_divisores(B)==A:
        return True
    else:
        return False
'''
def sao_amigos (A,B):
    return soma_dos_divisores(A)==B and soma_dos_divisores(B)==A
'''
def resposta_s_ou_n_para_uma_pergunta (pergunta):
    digitou_corretamente=False
    while not digitou_corretamente:
        resposta=input(pergunta)
        resposta=resposta.upper()
        # if len(resposta)!=1 or resposta not in "SN":
        # if resposta not in ["S","N"]
        if resposta!="S" and resposta!="N":
            print("Deve-se responder S ou N; tente novamente!")
        else:
            digitou_corretamente=True 
            
    return resposta

# daqui para cima definimos subprogramas
# daqui para baixo chamamos o que definimos para formar o programa
    
print('PROGRAMA PARA VERIFICAR SE DOIS NÚMERO NATURAIS SÃO AMIGOS')

terminou_de_testar_amigos=False
while not terminou_de_testar_amigos:
    # obtendo o primeiro_numero
    digitou_corretamente=False
    while not digitou_corretamente:
        try:
            primeiro_numero=int(input("Digite um número natural: "))
        except ValueError:
            print("Deve-se digitar um número natural; tente novamente!")
        else:
            if primeiro_numero<0:
                print("Negativos não são números naturais; tente novamente!")
            else:
                digitou_corretamente=True
    
    # obtendo o segundo_numero
    digitou_corretamente=False
    while not digitou_corretamente:
        try:
            segundo_numero=int(input("Digite OUTRO número natural: "))
        except ValueError:
            print("Deve-se digitar um número natural; tente novamente!")
        else:
            if segundo_numero<0:
                print("Negativos não são números naturais; tente novamente!")
            else:
                if segundo_numero==primeiro_numero:
                    print("Foi pedido OUTRO número natural, não o mesmo; tente novamente!")
                else:
                    digitou_corretamente=True
    
    # se a soma dos divisores de um deu igual ao outro e vice-versa diga que são amigos
    # senão, diga que não são amigos
    if sao_amigos(primeiro_numero,segundo_numero):
        print(primeiro_numero,"e",segundo_numero,"SÃO amigos!")
    else:
        print(primeiro_numero,"e",segundo_numero,"NÃO são amigos!")
        
    if resposta_s_ou_n_para_uma_pergunta("Deseja verificar se outro par de números são amigos (S/N)? ")=="N":
        terminou_de_testar_amigos=True
        
print("PROGRAMA ENCERRADO")   