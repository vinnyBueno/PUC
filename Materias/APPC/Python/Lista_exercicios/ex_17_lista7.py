def posicao_mais_direita(txt, TXT):
    ultima_posicao = 0

    for i in range(len(txt) - len(TXT) + 1):


        for j in range(len(TXT)):
            if txt[i + j] != TXT[j]:
                break

        else:
            ultima_posicao = i

    return ultima_posicao


print(posicao_mais_direita("abcPUCdePUCfghiPUCjk", "PUC"))
