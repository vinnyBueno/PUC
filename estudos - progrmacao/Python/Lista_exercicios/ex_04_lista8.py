def media_notas (lista):
    soma = 0
    i = 0

    while i < len(lista):
        soma += lista[i]["nota"]
        i += 1

    media = soma / len(lista)

    return media

lista = [
    {"disciplina": "Algoritmos", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Banco", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Python", "nota": 9.5, "frequencia": 95}
]

print(media_notas(lista))