disciplinas = [["Matemática", 8.5, 75],["Português", 7.0, 80],["História", 6.0, 65],["Programação", 9.2, 90]]

def materiaMaiorNota(disc):
    if not disc:
        return None

    nomeMateriaMaiorNota = disc[0]

    for disciplina in disc:
        if disciplina[1] > nomeMateriaMaiorNota[1]:
            nomeMateriaMaiorNota = disciplina
    return nomeMateriaMaiorNota

resultado = materiaMaiorNota(disciplinas)
print(resultado)