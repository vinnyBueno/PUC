lista = [
    {"disciplina": "Algoritmos", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Banco", "nota": 5.0, "frequencia": 85},
    {"disciplina": "Python", "nota": 9.5, "frequencia": 95},
    {"disciplina": "Redes", "nota": 10.0, "frequencia": 70}
]

def disciplinas_aprovadas(lista):
    aprovados = 0
    i = 0
    while i < len(lista):
        if lista[i]['nota'] >= 6 and lista[i]['frequencia'] >= 75:
            aprovados += 1
        i += 1

    return aprovados

print(disciplinas_aprovadas(lista))