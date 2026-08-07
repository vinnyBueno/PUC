def materia_maior_nota(lista):
    maior_nota = lista[0]["nota"]
    nome_disciplina = lista[0]["disciplina"]

    i = 1
    while i < len(lista):
        if lista[i]["nota"] > maior_nota:
            maior_nota = lista[i]["nota"]
            nome_disciplina = lista[i]["disciplina"]
        i += 1
    return nome_disciplina

lista = [
    {"disciplina": "Algoritmos", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Banco", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Python", "nota": 9.5, "frequencia": 95}
]

print(materia_maior_nota(lista))