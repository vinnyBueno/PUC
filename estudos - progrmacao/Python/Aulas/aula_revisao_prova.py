aluno = [[26262626, "João", 1919191919, "joão@puccampinas.edu.br"], [25252525, "Ana", 1181818188, "ana@puccampinas.edu.br"]]

disciplina = [[123, "APPC", 4], [234, "EPBD", 2]]

resultado = [[26262626, 123, 1, 2026, 7.5, 0.85], [26262626, 234, 1, 2026, 6.5, 0.75],
             [25252525, 134, 1, 2025, 3.0, 0.80], [25252525, 123, 1, 2026, 7.0, 0.85]]

def nomeAunoMaiorNota (alu, res):
    resMaiorNota = res[0]
    posicao = 1
    while posicao < len(alu):
        if alu[posicao][4] > resMaiorNota[4]:
            resMaiorNota = res[posicao]
        posicao += 1
    raAlunoMaiorNota = resMaiorNota[0]
    posicao = 0
    while posicao < len(alu):
        if raAlunoMaiorNota == alu[posicao][0]:
            return alu[posicao][1]


def discMenorFrec (disc, res):
    resmenorfreq = res[5]
    posicao = 1
    while posicao < len(res):
        if disc[posicao][5] < resmenorfreq[5]:
            resmenorfreq = res[posicao]
            posicao+=1
    codDisMenorFreq=resmenorfreq[1]
    posicao=0
    while posicao<len(disc):
        if codDisMenorFreq==disc[posicao][0]:
            return disc[posicao][1]
        posicao+=1

print (nomeAunoMaiorNota(aluno, resultado))