def materia_menor_frequencia(lista):
    nome_disciplina = lista[0]["disciplina"]
    menor_frequencia = lista[0]["frequencia"]
    i = 1
    while i < len(lista):
        if menor_frequencia > lista[i]["frequencia"]:
            menor_frequencia = lista[i]["frequencia"]
            nome_disciplina = lista[i]["disciplina"]
        i += 1
    return nome_disciplina


lista = [
    {"disciplina": "Algoritmos", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Banco", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Python", "nota": 9.5, "frequencia": 95}
]

print(materia_menor_frequencia(lista))