def soma_notas (lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma += lista[i]['nota']
        i += 1
    return soma

lista = [
    {"disciplina": "Algoritmos", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Banco", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Python", "nota": 9.5, "frequencia": 95}
]

print(soma_notas(lista))