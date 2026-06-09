def conversao(texto):
    resultado = ''
    i = 0
    while i < len(texto):
        if ord(texto[i]) >= 65 and ord(texto[i]) <= 90:
            codigo = ord(texto[i])
            resultado += chr(codigo + 32)
        else:
            resultado += texto[i]
        i += 1
    return resultado


print(conversao("Python"))