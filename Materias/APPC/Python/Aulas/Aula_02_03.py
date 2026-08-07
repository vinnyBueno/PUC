# Aula refetente ao dia 02/03/2026

# versão 1
'''
print("PROGRAMA PARA CALCULAR AREAS DE QUADRADOS")

lado_com_texto = input("\nDigite o quanto mede em cm o lado do quadrado desejado: ")

ladoComNumero = float(lado_com_texto)
area = ladoComNumero*ladoComNumero

print(f"A area do quadrado indicado é de {area} centimetro quadrados!")

print("\nPROGRAMA ENCERRADO COM SUCESSO!")
'''

# versão 2
'''
print("PROGRAMA PARA CALCULAR AREAS DE QUADRADOS")

lado = float(input("\nDigite o quanto mede em cm o lado do quadrado desejado: "))

area = lado*lado

print(f"A area do quadrado indicado é de {area} centimetro quadrados!")

print("\nPROGRAMA ENCERRADO COM SUCESSO!")
'''
# versão 3 

print("PROGRAMA PARA CALCULAR AREAS DE QUADRADOS")

print("Digite quanto mede em cm o lado do quadrado desejado: ", end="") #end="" faz com que o print não termine pulando uma linha

lado = float(input())

area = lado*lado

print("A area do quadrado indicado é de",area, "centimetro quadrados!", sep=" ") # sep="" define o separador no lugar das virgulas

print("\nPROGRAMA ENCERRADO COM SUCESSO!")


#tarefa: pesquisar como converter graus celcios em farenhaints

