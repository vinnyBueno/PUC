def contrario(texto):
    resultado = ''
    i = len(texto) -1
    while i >= 0:
        resultado += texto[i]
        i -= 1
    return resultado

print(contrario("python"))