lista = [
    {"disciplina": "Algoritmos", "nota": 10.0, "frequencia": 95},
    {"disciplina": "Banco", "nota": 5.0, "frequencia": 85},
    {"disciplina": "Python", "nota": 9.5, "frequencia": 95},
    {"disciplina": "Redes", "nota": 10.0, "frequencia": 70}
]

def disciplinas_aprovadas(lista):
    aprovados = 0
    maior_nota = -1
    disciplina_maior_nota = ''
    i = 0
    while i < len(lista):
        if lista[i]['nota'] >= 6 and lista[i]['frequencia'] >= 75:
            aprovados += 1
            if lista[i]['nota'] > maior_nota:
                maior_nota = lista[i]['nota']
                disciplina_maior_nota = lista[i]['disciplina']
        i += 1

    return disciplina_maior_nota

print(disciplinas_aprovadas(lista))